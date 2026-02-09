from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AttendanceForm
from .models import Attendance

# Create your views here.
def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)

            # 🔥 Assign business from logged-in user
            attendance.business_profile = request.user.business_profile
            attendance.save()

            return redirect('Dashboard:dashboard_view')  # change as needed
    else:
        form = AttendanceForm()

    return render(request, 'Attendance.html', {'form': form})




def Attendance_list_view(request):
    attendance_records = Attendance.objects.all()
    context = {
        'attendance_records': attendance_records
    }
    return context