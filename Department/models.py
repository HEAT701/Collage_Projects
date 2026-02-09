from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    business_profile = models.ForeignKey(
        'Employee.BusinessProfile',
        on_delete=models.CASCADE,
        related_name='departments'
    )
    def total_employees(self):
        return self.employees.count()
    
    def __str__(self):
        return self.name