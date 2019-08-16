from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

def register_user(request,email,first_name,last_name,password):
    try:
        user = User.objects.create_user(username=email,password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        auth = authenticate(request,username=email,password=password)
        login(request,user)
        user_role.objects.create(user=request.user,management_role=False)
        return "success"
    except:
        return "email_already_exists"

def login_user(request,email,password,scope):
    user = authenticate(request,username=email,password=password)
    if user is not None:
        login(request,user)
        if scope == user_role.objects.get(user=request.user).management_role:
            return "success"
        else:
            logout(user)
            return "invalid_credentials"
    else:
        return "invaid_credentials"

def basic_functions(request):
    try:
        if request.GET['logout'] == 'true':
            logout(request)
    except:
        pass
