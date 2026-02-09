from django.shortcuts import render,redirect
from .forms import DepartmentForm

from django.contrib import messages
from .models import Department
# Create your views here.
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




def Department_detail_view(request, department_id):
    department = Department.objects.get(id=department_id)
    context = {
        'department': department
    }
    return render(request, 'Department_Detail.html', context)
  


# department delete and update views are not created because there is no such requirement in the project.

def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    messages.success(request, 'Department deleted successfully.')
    return redirect('Dashboard:dashboard_view')
