from django.contrib import admin
from .models import Employee,BusinessProfile
# Register your models here.
admin.site.register(BusinessProfile)
admin.site.register(Employee)