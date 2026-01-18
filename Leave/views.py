from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import LeaveForm
from .models import Leave
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

def leave_Management_view(request, leave_id, action):
    try:
        leave_request = Leave.objects.get(leave_id=leave_id)
        if action == 'approve':
            leave_request.status = 'APPROVED'
        elif action == 'reject':
            leave_request.status = 'REJECTED'
        leave_request.save()
        return True
    except Leave.DoesNotExist:
        return False
