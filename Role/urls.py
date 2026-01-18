from django.urls import path
from .views import Job_view
urlpatterns = [
    path('Job/', Job_view, name='Job')
]