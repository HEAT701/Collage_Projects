from .models import Department

from django.forms import ModelForm

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        