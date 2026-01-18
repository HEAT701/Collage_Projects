from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm


# Create your views here.
def Project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    return render(request, 'Project.html', {'form': form})