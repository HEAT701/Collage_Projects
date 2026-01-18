from django.urls import path
from .views import Department_view
urlpatterns = [
    path('Department/', Department_view, name='Department'),
]