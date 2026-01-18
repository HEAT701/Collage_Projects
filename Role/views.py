from django.shortcuts import render,redirect
from .models import Job
from.forms import JobForm

# Create your views here.
def Job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, 'Job.html', {'form': form})