from django.db import models
from django.core.exceptions import ValidationError
from Employee.models import BusinessProfile
class Leave(models.Model):
    LEAVE_STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    LEAVE_TYPE = (
        ('casual', 'Casual'),
        ('sick', 'Sick'),
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    )

    employee = models.ForeignKey(
        'Employee.Employee',
        on_delete=models.CASCADE,
        related_name='leaves'
    )

    business_profile = models.ForeignKey(
        BusinessProfile,
        on_delete=models.CASCADE,
        related_name='leaves'
    )

    leave_type = models.CharField(
        max_length=10,
        choices=LEAVE_TYPE
    )

    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=LEAVE_STATUS,
        default='pending'
    )

    approved_by = models.ForeignKey(
        'Employee.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_leaves'
    )

    applied_on = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

        if self.employee.business_profile != self.business_profile:
            raise ValidationError(
                "Employee must belong to the same business as the leave"
            )

    def __str__(self):
        return f"{self.employee.username} ({self.leave_type}) - {self.start_date} to {self.end_date}"
