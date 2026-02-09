from django.urls import path
from .views import attendance_create
app_name = 'Attendance'
urlpatterns = [
    path('Attendance/', attendance_create, name='attendance_create'),
]

