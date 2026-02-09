from datetime import date, datetime
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
        'Employee.BusinessProfile',
        on_delete=models.CASCADE,
        related_name='attendance',
        null=True,
        blank=True
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

        if self.employee_id and self.business_profile_id:
            if self.employee.business_profile_id != self.business_profile_id:
                raise ValidationError(
                    "Employee must belong to the same business as attendance record"
                )
            
    def save(self, *args, **kwargs):
        if not self.business_profile and self.employee:
            self.business_profile = self.employee.business_profile
        super().save(*args, **kwargs)

    def Total_hours(self):
        if self.check_in and self.check_out:
            delta = datetime.combine(date.min, self.check_out) - datetime.combine(date.min, self.check_in)
            return delta
        return None
    def __str__(self):
        return f"{self.employee.username} - {self.date}"
