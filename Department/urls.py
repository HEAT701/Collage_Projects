from django.urls import path
from .views import Department_view,Department_detail_view,delete_department
from .models import Department
app_name = 'Department'
urlpatterns = [
    path('create_department/', Department_view, name='create_department'),
    path('department/<int:department_id>/', Department_detail_view, name='department_detail'),
    path('department/<int:department_id>/delete/', delete_department, name='delete_department'),
]