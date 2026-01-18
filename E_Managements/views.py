from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home_view(request):
    return render(request,"Home.html")