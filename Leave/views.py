from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import LeaveForm
from .models import Leave
from django.contrib import messages
# Create your views here.

def Leave_view(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = LeaveForm()
    return render(request, 'Leave.html', {'form': form})


# Manage Leave Request 

def manage_leave(request, leave_id, action):
    leave = Leave.objects.get(pk=leave_id)

    if action == 'approve':
        leave.status = 'approved'
        leave.approved_by = request.user
    elif action == 'reject':
        leave.status = 'rejected'

    leave.save()
    return redirect('Dashboard:dashboard_view')





def Employee_leave_apply_view(request):
    if request.method == 'POST':
        leave_type = request.POST.get('leave_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        # ✅ yahan sirf Employee object lena hai
        employee = request.user.employee

        Leave.objects.create(
            employee=employee,                       # ✅ correct
            business_profile=employee.business_profile,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status='pending'
        )
        employee.save()
        return HttpResponse("Leave request submitted successfully")

    return HttpResponse("Invalid request method")

# total leave types

