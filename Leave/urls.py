from django.urls import path
from .views import Leave_view,leave_Management_view
app_name = 'Leave'
urlpatterns =[
    path('Leave/', Leave_view, name='Leave'),
    path('manage_leave/<int:leave_id>/<str:action>/', leave_Management_view, name='manage_leave'),
]