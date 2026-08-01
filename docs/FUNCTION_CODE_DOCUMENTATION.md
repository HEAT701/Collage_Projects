# Function Code Documentation (All Apps)

This document lists function/method definitions found in the repository apps, along with location, signature, and code snippet.

## Apps Covered

- **Employee**: 9 functions/methods
- **Department**: 5 functions/methods
- **Role**: 2 functions/methods
- **Project**: 2 functions/methods
- **Leave**: 5 functions/methods
- **Attendance**: 7 functions/methods
- **Dashboard**: 7 functions/methods
- **Login_App**: 2 functions/methods
- **E_Managements**: 1 functions/methods

---

## Employee App

### File: `Employee/models.py`

#### 1. `BusinessProfile.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Employee/models.py:13-14`
- **Code:**
```python
def __str__(self):
        return self.business_name
```

#### 2. `Employee.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Employee/models.py:66-67`
- **Code:**
```python
def __str__(self):
        return self.username
```

### File: `Employee/servies.py`

#### 1. `Get_Employee_view` (function)
- **Signature:** `Get_Employee_view(request)`
- **Location:** `Employee/servies.py:7-9`
- **Code:**
```python
def Get_Employee_view(request):
   get_Enployee = Employee.objects.filter(roal='employee', is_active=True)
   return get_Enployee
```

### File: `Employee/views.py`

#### 1. `Create_Employeeview` (function)
- **Signature:** `Create_Employeeview(request)`
- **Location:** `Employee/views.py:15-79`
- **Code:**
```python
def Create_Employeeview(request):
    business = request.user.business_profile

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        salary = request.POST.get('salary')
        salary = Decimal(salary) if salary else None

        job_id = request.POST.get('job')
        department_id = request.POST.get('department')

        department = Department.objects.filter(
            id=department_id,
            business_profile=business
        ).first()

        job = Job.objects.filter(
            id=job_id,
            business_profile=business
        ).first()

        
        if Employee.objects.filter(email=email).exists():
            messages.error(request, 'An employee with this email already exists.')
            return redirect('Employee:create_employee')
        try:
            employee = Employee.objects.create_user(
                username = email,
                email=email,
                password='Test@1234',
                first_name=first_name,
                last_name=last_name,
            )
        except IntegrityError :
            messages.error(request, 'An employee with this username already exists.')
            return redirect('Employee:create_employee')
        employee.phone = phone
        employee.hire_date = hire_date
        employee.salary = salary
        employee.business_profile = business
        employee.role = 'employee'
        employee.department = department
        employee.job = job
        employee.save()
        messages.success(request, 'Employee created successfully.')
        return redirect('Dashboard:dashboard_view')

    # ✅ Correct filtering (NEW model design)
    departments = Department.objects.filter(
        business_profile=business
    )

    jobs = Job.objects.filter(
        business_profile=business
    )

    return render(request, 'Create_Employee.html', {
        'departments': departments,
        'jobs': jobs
    })
```

#### 2. `Employee_List_view` (function)
- **Signature:** `Employee_List_view(request)`
- **Location:** `Employee/views.py:82-87`
- **Code:**
```python
def Employee_List_view(request):
    Employees = Get_Employee_view(request)
    context = {
        'Employees': Employees
    }
    return render(request, 'Employee_Dashboard.html', context)
```

#### 3. `Owner_register` (function)
- **Signature:** `Owner_register(request)`
- **Location:** `Employee/views.py:93-113`
- **Code:**
```python
def Owner_register(request):
    if request.method == 'POST':
        owner = Employee.objects.create_user(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            role='owner',
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        business = BusinessProfile.objects.create(
            business_name=request.POST.get('business_name'),
            business_address=request.POST.get('business_address'),
            business_phone=request.POST.get('business_phone'),
            business_email=request.POST.get('business_email'),
        )
        owner.business_profile = business
        owner.save()
        return redirect('Home')
    return render(request, 'Owner_register.html')
```

#### 4. `Employee_Detail_view` (function)
- **Signature:** `Employee_Detail_view(request, employee_id)`
- **Location:** `Employee/views.py:118-123`
- **Code:**
```python
def Employee_Detail_view(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'Employee_Detail.html', context)
```

#### 5. `Employee_Delete_view` (function)
- **Signature:** `Employee_Delete_view(request, employee_id)`
- **Location:** `Employee/views.py:125-129`
- **Code:**
```python
def Employee_Delete_view(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('Dashboard:dashboard_view')
```

#### 6. `Employee_Update_view` (function)
- **Signature:** `Employee_Update_view(request, employee_id)`
- **Location:** `Employee/views.py:132-182`
- **Code:**
```python
def Employee_Update_view(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    business = request.user.business_profile

    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            
            job_id = request.POST.get('job')
            department_id = request.POST.get('department')

            # Filter department and job by business profile for security
            if department_id:
                employee.department = Department.objects.filter(
                    id=department_id,
                    business_profile=business
                ).first()

            if job_id:
                employee.job = Job.objects.filter(
                    id=job_id,
                    business_profile=business
                ).first()

            employee.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('Employee:employee_detail', employee_id=employee.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeUpdateForm(instance=employee)

    # Filter departments and jobs by business profile
    departments = Department.objects.filter(
        business_profile=business
    )

    jobs = Job.objects.filter(
        business_profile=business
    )

    # Update form querysets to show only business-specific options
    form.fields['department'].queryset = departments
    form.fields['job'].queryset = jobs

    context = {
        'form': form,
        'employee': employee,
    }
    return render(request, 'Employee_Update.html', context)
```

---

## Department App

### File: `Department/models.py`

#### 1. `Department.total_employees` (method)
- **Signature:** `total_employees(self)`
- **Location:** `Department/models.py:13-14`
- **Code:**
```python
def total_employees(self):
        return self.employees.count()
```

#### 2. `Department.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Department/models.py:16-17`
- **Code:**
```python
def __str__(self):
        return self.name
```

### File: `Department/views.py`

#### 1. `Department_view` (function)
- **Signature:** `Department_view(request)`
- **Location:** `Department/views.py:7-18`
- **Code:**
```python
def Department_view(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            depart = form.save(commit=False)
            depart.business_profile = request.user.business_profile
            depart.save()
            return redirect('Dashboard:dashboard_view')
    context ={
        'form': DepartmentForm()
    }
    return render(request, 'Department.html',context)
```

#### 2. `Department_detail_view` (function)
- **Signature:** `Department_detail_view(request, department_id)`
- **Location:** `Department/views.py:23-28`
- **Code:**
```python
def Department_detail_view(request, department_id):
    department = Department.objects.get(id=department_id)
    context = {
        'department': department
    }
    return render(request, 'Department_Detail.html', context)
```

#### 3. `delete_department` (function)
- **Signature:** `delete_department(request, department_id)`
- **Location:** `Department/views.py:34-38`
- **Code:**
```python
def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    messages.success(request, 'Department deleted successfully.')
    return redirect('Dashboard:dashboard_view')
```

---

## Role App

### File: `Role/models.py`

#### 1. `Job.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Role/models.py:10-11`
- **Code:**
```python
def __str__(self):
        return self.title
```

### File: `Role/views.py`

#### 1. `Job_view` (function)
- **Signature:** `Job_view(request)`
- **Location:** `Role/views.py:6-19`
- **Code:**
```python
def Job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.business_profile = request.user.business_profile
            job.save()
            return redirect('Dashboard:dashboard_view')
    else:
        form = JobForm()
    context = {
        'form': form
    }
    return render(request, 'Job.html',context)
```

---

## Project App

### File: `Project/models.py`

#### 1. `Project.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Project/models.py:22-23`
- **Code:**
```python
def __str__(self):
        return self.name
```

### File: `Project/views.py`

#### 1. `Project_view` (function)
- **Signature:** `Project_view(request)`
- **Location:** `Project/views.py:7-13`
- **Code:**
```python
def Project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, 'Project.html', {'form': form})
```

---

## Leave App

### File: `Leave/models.py`

#### 1. `Leave.clean` (method)
- **Signature:** `clean(self)`
- **Location:** `Leave/models.py:55-62`
- **Code:**
```python
def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

        if self.employee.business_profile != self.business_profile:
            raise ValidationError(
                "Employee must belong to the same business as the leave"
            )
```

#### 2. `Leave.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Leave/models.py:64-65`
- **Code:**
```python
def __str__(self):
        return f"{self.employee.username} ({self.leave_type}) - {self.start_date} to {self.end_date}"
```

### File: `Leave/views.py`

#### 1. `Leave_view` (function)
- **Signature:** `Leave_view(request)`
- **Location:** `Leave/views.py:8-16`
- **Code:**
```python
def Leave_view(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = LeaveForm()
    return render(request, 'Leave.html', {'form': form})
```

#### 2. `manage_leave` (function)
- **Signature:** `manage_leave(request, leave_id, action)`
- **Location:** `Leave/views.py:21-31`
- **Code:**
```python
def manage_leave(request, leave_id, action):
    leave = Leave.objects.get(pk=leave_id)

    if action == 'approve':
        leave.status = 'approved'
        leave.approved_by = request.user
    elif action == 'reject':
        leave.status = 'rejected'

    leave.save()
    return redirect('Dashboard:dashboard_view')
```

#### 3. `Employee_leave_apply_view` (function)
- **Signature:** `Employee_leave_apply_view(request)`
- **Location:** `Leave/views.py:37-59`
- **Code:**
```python
def Employee_leave_apply_view(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        # ✅ yahan sirf Employee object lena hai
        employee = request.user.employee

        Leave.objects.create(
            employee=employee,                       # ✅ correct
            business_profile=employee.business_profile,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status='pending'
        )
        employee.save()
        return HttpResponse("Leave request submitted successfully")

    return HttpResponse("Invalid request method")
```

---

## Attendance App

### File: `Attendance/forms.py`

#### 1. `AttendanceForm.save` (method)
- **Signature:** `save(self, commit)`
- **Location:** `Attendance/forms.py:11-21`
- **Code:**
```python
def save(self, commit=True):
        attendance = super().save(commit=False)

        # safety (model already handles this, but extra protection)
        if not attendance.business_profile and attendance.employee:
            attendance.business_profile = attendance.employee.business_profile

        if commit:
            attendance.save()

        return attendance
```

### File: `Attendance/models.py`

#### 1. `Attendance.clean` (method)
- **Signature:** `clean(self)`
- **Location:** `Attendance/models.py:40-49`
- **Code:**
```python
def clean(self):
        if self.check_in and self.check_out:
            if self.check_out < self.check_in:
                raise ValidationError("Check-out time cannot be before check-in")

        if self.employee_id and self.business_profile_id:
            if self.employee.business_profile_id != self.business_profile_id:
                raise ValidationError(
                    "Employee must belong to the same business as attendance record"
                )
```

#### 2. `Attendance.save` (method)
- **Signature:** `save(self, *args, **kwargs)`
- **Location:** `Attendance/models.py:51-54`
- **Code:**
```python
def save(self, *args, **kwargs):
        if not self.business_profile and self.employee:
            self.business_profile = self.employee.business_profile
        super().save(*args, **kwargs)
```

#### 3. `Attendance.Total_hours` (method)
- **Signature:** `Total_hours(self)`
- **Location:** `Attendance/models.py:56-60`
- **Code:**
```python
def Total_hours(self):
        if self.check_in and self.check_out:
            delta = datetime.combine(date.min, self.check_out) - datetime.combine(date.min, self.check_in)
            return delta
        return None
```

#### 4. `Attendance.__str__` (method)
- **Signature:** `__str__(self)`
- **Location:** `Attendance/models.py:61-62`
- **Code:**
```python
def __str__(self):
        return f"{self.employee.username} - {self.date}"
```

### File: `Attendance/views.py`

#### 1. `attendance_create` (function)
- **Signature:** `attendance_create(request)`
- **Location:** `Attendance/views.py:7-21`
- **Code:**
```python
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)

            # 🔥 Assign business from logged-in user
            attendance.business_profile = request.user.business_profile
            attendance.save()

            return redirect('Dashboard:dashboard_view')  # change as needed
    else:
        form = AttendanceForm()

    return render(request, 'Attendance.html', {'form': form})
```

#### 2. `Attendance_list_view` (function)
- **Signature:** `Attendance_list_view(request)`
- **Location:** `Attendance/views.py:26-31`
- **Code:**
```python
def Attendance_list_view(request):
    attendance_records = Attendance.objects.all()
    context = {
        'attendance_records': attendance_records
    }
    return context
```

---

## Dashboard App

### File: `Dashboard/servies.py`

#### 1. `count_employee_view` (function)
- **Signature:** `count_employee_view(request)`
- **Location:** `Dashboard/servies.py:13-15`
- **Code:**
```python
def count_employee_view(request):
    employee_count = Employee.objects.filter(business_profile=request.user.business_profile, role='employee', is_active=True).count()
    return employee_count
```

#### 2. `get_recent_added_employees` (function)
- **Signature:** `get_recent_added_employees(user)`
- **Location:** `Dashboard/servies.py:17-21`
- **Code:**
```python
def get_recent_added_employees(user):
    return Employee.objects.filter(
        business_profile=user.business_profile,
        role='employee'
    ).order_by('-date_joined')[:3]
```

#### 3. `fiend_Total_deparment` (function)
- **Signature:** `fiend_Total_deparment(request)`
- **Location:** `Dashboard/servies.py:29-31`
- **Code:**
```python
def fiend_Total_deparment(request):
    total_departments = Department.objects.filter(business_profile=request.user.business_profile)
    return total_departments
```

#### 4. `today_attendance_view` (function)
- **Signature:** `today_attendance_view(request)`
- **Location:** `Dashboard/servies.py:42-45`
- **Code:**
```python
def today_attendance_view(request):
    today = timezone.now().date()
    today_attendance = Attendance.objects.filter(business_profile=request.user.business_profile, date=today)
    return today_attendance
```

#### 5. `Get_pending_leave_view` (function)
- **Signature:** `Get_pending_leave_view(request)`
- **Location:** `Dashboard/servies.py:53-55`
- **Code:**
```python
def Get_pending_leave_view(request):
    pending_leaves = Leave.objects.filter(status='pending', business_profile=request.user.business_profile)
    return pending_leaves
```

### File: `Dashboard/views.py`

#### 1. `Dashboard_view` (function)
- **Signature:** `Dashboard_view(request)`
- **Location:** `Dashboard/views.py:7-19`
- **Code:**
```python
def Dashboard_view(request):
    count = count_employee_view(request)
    departments = fiend_Total_deparment(request)
    context = {
        'total_employees': count,
        'Total_departments': departments,
        'today_attendance': today_attendance_view(request),
        'pending_leaves': Get_pending_leave_view(request).count(),
        'pending_leave_list': Get_pending_leave_view(request),
        'recentadd_employees':get_recent_added_employees(request.user),

    }
    return render(request, 'dashboard.html', context)
```

#### 2. `Employee_Dashboard_view` (function)
- **Signature:** `Employee_Dashboard_view(request)`
- **Location:** `Dashboard/views.py:22-26`
- **Code:**
```python
def Employee_Dashboard_view(request):
    context = {
        'leave_types': Leave.objects.values_list('leave_type', flat=True).distinct()
    }
    return render(request, 'Employee_Dashboard.html', context)
```

---

## Login_App App

### File: `Login_App/views.py`

#### 1. `login_view` (function)
- **Signature:** `login_view(request)`
- **Location:** `Login_App/views.py:7-20`
- **Code:**
```python
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return HttpResponse("Invalid username or password")
        if user.role == 'owner':
            login(request, user)
            return redirect('Dashboard:dashboard_view')
        elif user.role == 'employee':
            login(request, user)
            return redirect('Dashboard:employee_dashboard')
    return render(request, 'Login.html')
```

#### 2. `logout_view` (function)
- **Signature:** `logout_view(request)`
- **Location:** `Login_App/views.py:22-24`
- **Code:**
```python
def logout_view(request):
    logout(request)
    return redirect('Home')
```

---

## E_Managements App

### File: `E_Managements/views.py`

#### 1. `Home_view` (function)
- **Signature:** `Home_view(request)`
- **Location:** `E_Managements/views.py:5-6`
- **Code:**
```python
def Home_view(request):
    return render(request,"Home.html")
```
