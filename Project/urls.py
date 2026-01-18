from django.urls import path
from .views import Project_view
urlpatterns = [
    path('Project/', Project_view, name='Project')
]