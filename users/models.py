from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField (max_length=100)
    department = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    email_address = models.TextField(blank=True, null=True)
   
  
    def __str__(self):
        return self.name