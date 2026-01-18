
from django.urls import path
from .views import Create_Employeeview,Employee_List_view,Owner_register
app_name = 'Employee'
urlpatterns = [
    path('owner_register/', Owner_register, name='owner_register'),
    path('create_employee/', Create_Employeeview, name='create_employee'),
    path('employee_dashboard/', Employee_List_view, name='Employee_Dashboard'),
]
