from django.http import HttpResponse
from Employee.models import Employee
from django.contrib.auth.decorators import login_required


#--------------->----------------This is Employees Management sections ------------------------#
'''
def Get_Employee_view(request):
   get_Enployee = Employee.objects.filter(roal='employee', is_active=True)
   return get_Enployee
'''
@login_required
def count_employee_view(request):
    employee_count = Employee.objects.filter(business_profile=request.user.business_profile, role='employee', is_active=True).count()
    return employee_count
'''
def Resent_Added_Employee_view(request):
    recent_employees = Employee.objects.filter(roal='employee', is_active=True).order_by('-date_joined')[:5]
    return recent_employees
'''



#--------------->-------------- This section to manage Department section app -------------------#

from Department.models import Department
@login_required
def fiend_Total_deparment(request):
    business = request.user.business_profile

    total_depart = Department.objects.filter(
        employees__business_profile=business,
        employees__is_active=True
    ).distinct().count()

    return total_depart



# ----------------->-------------- This is department sections--------------#
from Attendance.models import Attendance
from django.utils import timezone
# today attendace employee
@login_required
def today_attendance_view(request):
    today = timezone.now().date()
    today_attendance = Attendance.objects.filter(date=today).count()
    return today_attendance




# --------------->----------------This is Leave  sections ------------------------#
from Leave.models import Leave
@login_required
def Get_pending_leave_view(request):
    pending_leaves = Leave.objects.filter(status='pending').count()
    return pending_leaves

