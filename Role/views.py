from django.shortcuts import render,redirect
from .models import Job
from.forms import JobForm

# Create your views here.
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