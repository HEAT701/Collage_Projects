from django.urls import path
from .views import Job_view
app_name = 'Role'
urlpatterns = [
    path('Job_create/', Job_view, name='Job_create')
]