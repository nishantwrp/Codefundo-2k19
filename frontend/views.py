from django.shortcuts import render
from app.functions import *
from app.models import *
# Create your views here.

def indexView(request):
    basic_functions(request)
    return render(request,'index.html')

def userloginView(request):
    basic_functions(request)
    return render(request,'userlogin.html')

def userLoggedInView(request):
    basic_functions(request)
    if request.user.is_authenticated == True:
        context['success'] = True
    
    return render(request,'userloggedin.html')

def voterIDView(request):
    basic_functions(request)
    return render(request,'voterid.html')

def govloginView(request):
    basic_functions(request)
    if request.user.is_authenticated == True:
        context['success'] = True
    return render(request,'govlogin.html')

def registerView(request):
    basic_functions(request)
    context = {}
    if request.user.is_authenticated == True:
        context['success'] = True
    if 'check' in request.POST:
        if request.POST['password'] !=  request.POST['confirmpassword']:
            context['password_error'] = True
        else:
            r = register_user(request,request.POST['email'],request.POST['firstName'],request.POST['lastName'],request.POST['password'])
            if r != "success":
                context['register_error'] = True
            else:
                context['success'] = True
    return render(request,'signup.html',context=context)

def searchView(request):
    basic_functions(request)
    return render(request,'search.html')

def votedView(request):
    return render(request,'votedusers.html')

def reviewView(request):
    return render(request,'review.html')

def officialLoggedInView(request):
    return render(request,'officialloggedin.html')

def electionPortalView(request):
    return render(request,'electionportal.html')
