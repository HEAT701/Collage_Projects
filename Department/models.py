from django.db import models
from Employee.models import BusinessProfile


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    business_profile = models.ForeignKey(
        BusinessProfile,
        on_delete=models.CASCADE,
        related_name='departments'
    )

    def __str__(self):
        return self.name