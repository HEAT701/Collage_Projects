from .models import Employee


# Get all employees


def Get_Employee_view(request):
   get_Enployee = Employee.objects.filter(roal='employee', is_active=True)
   return get_Enployee