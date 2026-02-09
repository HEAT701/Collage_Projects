from django.forms import ModelForm
from .models import Attendance
from django import forms
from Employee.models import Employee
class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ['employee', 'status', 'date', 'check_in', 'check_out']

    def save(self, commit=True):
        attendance = super().save(commit=False)

        # safety (model already handles this, but extra protection)
        if not attendance.business_profile and attendance.employee:
            attendance.business_profile = attendance.employee.business_profile

        if commit:
            attendance.save()

        return attendance