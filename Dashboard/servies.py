from django.http import HttpResponse
from Employee.models import Employee
from django.contrib.auth.decorators import login_required


#--------------->----------------This is Employees Management sections ------------------------#
'''
def Get_Employee_view(request):
   get_Enployee = Employee.objects.filter(roal='employee', is_active=True)
   return get_Enployee
'''

def count_employee_view(request):
    employee_count = Employee.objects.filter(business_profile=request.user.business_profile, role='employee', is_active=True).count()
    return employee_count

def get_recent_added_employees(user):
    return Employee.objects.filter(
        business_profile=user.business_profile,
        role='employee'
    ).order_by('-date_joined')[:3]



#--------------->-------------- This section to manage Department section app -------------------#

from Department.models import Department

def fiend_Total_deparment(request):
    total_departments = Department.objects.filter(business_profile=request.user.business_profile)
    return total_departments



# ----------------->-------------- This is department sections--------------#
from Attendance.models import Attendance
from django.utils import timezone
# today attendace employee



def today_attendance_view(request):
    today = timezone.now().date()
    today_attendance = Attendance.objects.filter(business_profile=request.user.business_profile, date=today)
    return today_attendance




# --------------->----------------This is Leave  sections ------------------------#
from Leave.models import Leave

def Get_pending_leave_view(request):
    pending_leaves = Leave.objects.filter(status='pending', business_profile=request.user.business_profile)
    return pending_leaves


