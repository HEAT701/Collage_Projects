from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .servies import Get_Employee_view
from Employee.models import BusinessProfile
from Department.models import Department
from Role.models import Job
from django.shortcuts import render, redirect
from decimal import Decimal
from django.contrib import messages
from django.db import IntegrityError
from .forms import EmployeeUpdateForm


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


def Employee_List_view(request):
    Employees = Get_Employee_view(request)
    context = {
        'Employees': Employees
    }
    return render(request, 'Employee_Dashboard.html', context)



# create owner register view

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




def Employee_Detail_view(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    context = {
        'employee': employee
    }
    return render(request, 'Employee_Detail.html', context)

def Employee_Delete_view(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('Dashboard:dashboard_view')


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