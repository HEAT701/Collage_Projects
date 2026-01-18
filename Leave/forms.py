from django.forms import ModelForm
from Leave.models import Leave


class LeaveForm(ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'