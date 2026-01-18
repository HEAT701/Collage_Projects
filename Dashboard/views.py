from django.shortcuts import render
from .servies import count_employee_view,fiend_Total_deparment,today_attendance_view,Get_pending_leave_view
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Dashboard_view(request):
    count = count_employee_view(request)
    departments = fiend_Total_deparment(request)
    context = {
        'total_employees': count,
        'Total_departments': departments,
        'today_attendance': today_attendance_view(request),
        'pending_leaves': Get_pending_leave_view(request),

    }
    return render(request, 'dashboard.html', context)