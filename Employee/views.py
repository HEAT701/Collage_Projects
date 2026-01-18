from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .servies import Get_Employee_view
from Employee.models import BusinessProfile
from Department.models import Department
from Role.models import Job
def Create_Employeeview(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')

        job_id = request.POST.get('job')
        department_id = request.POST.get('department')

        job = Job.objects.get(id=job_id) if job_id else None
        department = Department.objects.get(id=department_id) if department_id else None

        Employee.objects.create_user(
            username=email,   # REQUIRED
            email=email,
            password='Temp@123',
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            hire_date=hire_date,
            salary=salary,
            job=job,
            department=department,
            business_profile=request.user.business_profile,
            role='employee'
        )

        return redirect('Home')
    departments = Department.objects.filter(
        employees__business_profile=request.user.business_profile
    ).distinct()

    jobs = Job.objects.all()

    return render(request, 'Create_Employee.html',{
        'departments': departments,
        'jobs': jobs
    })

# Create your views here.

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