from django.urls import path
from .views import Dashboard_view,Employee_Dashboard_view
app_name = 'Dashboard'
urlpatterns = [
    path('dashboard_view/',Dashboard_view,name="dashboard_view"),
    path('employee_dashboard_view/',Employee_Dashboard_view,name="employee_dashboard"),
]