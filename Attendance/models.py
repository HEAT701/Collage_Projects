from django.db import models
from django.core.exceptions import ValidationError
from Employee.models import BusinessProfile,Employee
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('half_day', 'Half Day'),
    )

    employee = models.ForeignKey(
        'Employee.Employee',
        on_delete=models.CASCADE,
        related_name='attendance'
    )

    business_profile = models.ForeignKey(
        BusinessProfile,
        on_delete=models.CASCADE,
        related_name='attendance'
    )

    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='present'
    )

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def clean(self):
        if self.check_in and self.check_out:
            if self.check_out < self.check_in:
                raise ValidationError("Check-out time cannot be before check-in")

        if self.employee.business_profile != self.business_profile:
            raise ValidationError(
                "Employee must belong to the same business as attendance record"
            )

    def __str__(self):
        return f"{self.employee.username} - {self.date}"
