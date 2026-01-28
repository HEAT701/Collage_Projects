from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AttendanceForm
from .models import Attendance

# Create your views here.
def Attendance_view(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    contex ={
        'form': AttendanceForm
    }
    return render(request, 'Attendance.html', contex)



# get all the attendance records
def Attendance_list_view(request):
    attendance_records = Attendance.objects.all()
    context = {
        'attendance_records': attendance_records
    }
    return context