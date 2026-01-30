from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

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

def logout_view(request):
    logout(request)
    return redirect('Home')