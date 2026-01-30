from django.shortcuts import render,redirect
from .forms import DepartmentForm
from .models import Department
# Create your views here.
def Department_view(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard:dashboard_view')
    context ={
        'form': DepartmentForm()
    }
    return render(request, 'Department.html',context)
