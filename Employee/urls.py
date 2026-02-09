
from django.urls import path
from .views import Create_Employeeview,Employee_List_view,Owner_register,Employee_Detail_view,Employee_Delete_view,Employee_Update_view
app_name = 'Employee'
urlpatterns = [
    path('owner_register/', Owner_register, name='owner_register'),
    path('create_employee/', Create_Employeeview, name='create_employee'),
    path('employee_dashboard/', Employee_List_view, name='Employee_Dashboard'),
    path('employee/<int:employee_id>/', Employee_Detail_view, name='employee_detail'),
    path('employee/<int:employee_id>/delete/', Employee_Delete_view, name='Employee_Delete'),
    path('employee/<int:employee_id>/update/', Employee_Update_view, name='Employee_Update'),
]
