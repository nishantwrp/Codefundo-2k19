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
    fathers_name = models.TextField()
    address = models.TextField()
    pincode = models.TextField()
    dob = models.TextField()
    mobile = models.TextField()
    contract_id = models.TextField()
    def __str__(self):
        return f'{self.aadhar} by {self.applicant.username}'

class azure_key(models.Model):
    name = models.TextField()
    key = models.TextField()


