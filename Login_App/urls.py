from django.urls import path
from .views import login_view
app_name = 'Login_App'
urlpatterns = [
    path('login_view/', login_view, name='login'),
]