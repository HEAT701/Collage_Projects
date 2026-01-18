from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from Department.models import Department
from Role.models import Job
class BusinessProfile(models.Model):
    business_name = models.CharField(max_length=100)
    business_address = models.CharField(max_length=255)
    business_phone = models.CharField(max_length=15)
    business_email = models.EmailField()

    def __str__(self):
        return self.business_name


class Employee(AbstractUser):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('owner', 'Owner'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    business_profile = models.ForeignKey(
        BusinessProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='employees'
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )   

    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees'
    )

    phone = models.CharField(max_length=15, null=True, blank=True)
    hire_date = models.DateField(default=now)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
