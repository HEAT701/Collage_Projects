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
            return HttpResponseRedirect('/login/?error=Invalid credentials')
        if user.role == 'owner':
            login(request, user)
            return redirect('dashboard')
        else:
            login(request, user)
            return redirect('Home')
    return render(request, 'login.html')