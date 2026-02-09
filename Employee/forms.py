from django import forms
from .models import Employee
from Department.models import Department
from Role.models import Job


class EmployeeUpdateForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        empty_label="Select Department"
    )
    
    job = forms.ModelChoiceField(
        queryset=Job.objects.all(),
        required=False,
        empty_label="Select Job"
    )

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone', 'hire_date', 'salary', 'department', 'job']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'hire_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Salary',
                'step': '0.01'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'job': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
