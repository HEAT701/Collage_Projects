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
            return redirect('create_employee')
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
            return redirect('create_employee')
        employee.phone = phone
        employee.hire_date = hire_date
        employee.salary = salary
        employee.business_profile = business
        employee.role = 'employee'
        employee.department = department
        employee.job = job
        employee.save()
        messages.success(request, 'Employee created successfully.')
        return redirect('dashboard')

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
        return redirect('dashboard')
    return render(request, 'Owner_register.html')