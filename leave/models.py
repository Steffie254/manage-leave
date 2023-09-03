from django.db import models

from users.models import Users

# Create your models here.

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    days = models.IntegerField(null=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name

class UserLeaves(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.PROTECT)
    days = models.IntegerField(null=True)
    days_remaining = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.user
    

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(UserLeaves, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.user} - {self.leave_type} - {self.status}"