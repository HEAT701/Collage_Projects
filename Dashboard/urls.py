from django.urls import path
from .views import Dashboard_view
urlpatterns = [
    path('dashboard_view',Dashboard_view,name="dashboard")
]