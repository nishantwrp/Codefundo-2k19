from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_role(models.Model):
    user = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    # Is Management
    management_role = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.user.username}'

class application(models.Model):
    applicant = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    aadhar = models.TextField()
    def __str__(self):
        return f'{self.user.aadhar}'

class azure_key(models.Model):
    name = models.TextField()
    key = models.TextField()


