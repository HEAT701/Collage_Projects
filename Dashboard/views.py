from django.shortcuts import render
from .servies import count_employee_view,fiend_Total_deparment,today_attendance_view,Get_pending_leave_view,get_recent_added_employees
from django.contrib.auth.decorators import login_required
from Leave.models import Leave
# Create your views here.
@login_required(login_url='Login_App:login/')
def Dashboard_view(request):
    count = count_employee_view(request)
    departments = fiend_Total_deparment(request)
    context = {
        'total_employees': count,
        'Total_departments': departments,
        'today_attendance': today_attendance_view(request),
        'pending_leaves': Get_pending_leave_view(request).count(),
        'pending_leave_list': Get_pending_leave_view(request),
        'recentadd_employees':get_recent_added_employees(request.user),

    }
    return render(request, 'dashboard.html', context)


def Employee_Dashboard_view(request):
    context = {
        'leave_types': Leave.objects.values_list('leave_type', flat=True).distinct()
    }
    return render(request, 'Employee_Dashboard.html', context)