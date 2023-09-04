from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users(AbstractUser):
   
    name = models.CharField(max_length=30, blank=True)
    # username = models.CharField(max_length=100, blank=True)
    gender = models.CharField (max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    phone_number = models.IntegerField()
    email_address = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True, null=True) 


    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = []
  
    def __str__(self):
        return self.name