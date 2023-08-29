from django.db import models

# Create your models here.

class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    days = models.IntegerField(null=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.name