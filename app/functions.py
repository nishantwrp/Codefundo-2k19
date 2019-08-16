from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register_user(request,email,first_name,last_name,password):
    try:
        user = User.objects.create_user(username=email,password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return login_user(request,email,password)
    except:
        return "email_already_exists"

def login_user(request,email,password):
    user = authenticate(request,username=email,password=password)
    if user is not None:
        login(request,user)
        return "success"
    else:
        return "invaid_credentials"