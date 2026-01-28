from django.urls import path
from .views import Department_view
app_name = 'Department'
urlpatterns = [
    path('create_department/', Department_view, name='create_department'),
]