from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import *
# Create your views here.

def initiateView(request):
    if len(azure_key.objects.filter(id=1)) == 0:
        User.objects.create_superuser("nishantwrp_2","","password")
        azure_key.objects.create(name="check",key="test")
    return JsonResponse({"message":"success"})
