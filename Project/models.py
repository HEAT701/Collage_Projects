from django.db import models
from Employee.models import BusinessProfile,Employee
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    business_profile = models.ForeignKey(
        BusinessProfile,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    employees = models.ManyToManyField(
        Employee,
        related_name='projects',
        blank=True
    )

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
