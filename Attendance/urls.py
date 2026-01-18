from django.urls import path
from .views import Attendance_view
urlpatterns = [
    path('Attendance/', Attendance_view, name='Attendance'),
]

