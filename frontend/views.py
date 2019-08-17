from django.shortcuts import render
from app.functions import *
from app.models import *
# Create your views here.

def indexView(request):
    context = {}
    basic_functions(request,context)    
    return render(request,'index.html',context=context)

def userloginView(request):
    context = {}
    basic_functions(request,context)
    only_unauthenticated(request,context)
    if 'check' in request.POST:
        r = login_user(request,request.POST['email'],request.POST['password'],False)
        if r != "success":
            context['invalid_error'] = True
        else:
            context['success'] = True
    return render(request,'userlogin.html',context=context)

def userLoggedInView(request):
    context = {}
    basic_functions(request,context)
    only_user(request,context)
    return render(request,'userloggedin.html',context=context)

def voterIDView(request):
    context = {}
    basic_functions(request,context)
    only_user(request,context)
    if 'check' in request.POST:
        r = application_form_submit(request,context,request.POST['FatherName'],request.POST['Address'],request.POST['Pincode'],request.POST['dob'],request.POST['mobile'],request.POST['aadhar'])
    return render(request,'voterid.html',context=context)

def govloginView(request):
    context = {}
    basic_functions(request,context)
    only_unauthenticated(request,context)
    if 'check' in request.POST:
        r = login_user(request,request.POST['username'],request.POST['password'],True)
        if r != 'success':
            context['invalid_error'] = True
        else:
            context['success'] = True
    return render(request,'govlogin.html',context=context)

def registerView(request):
    context = {}
    basic_functions(request,context)
    only_unauthenticated(request,context)
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
    context = {}
    basic_functions(request,context)
    only_user(request,context)
    return render(request,'search.html',context=context)

def votedView(request):
    context = {}
    basic_functions(request,context)
    return render(request,'votedusers.html',context=context)

def reviewView(request):
    context = {}
    basic_functions(request,context)
    only_official(request,context)
    try:
        if context['success'] == True:
            return render(request,'review.html',context=context)
    except:
        pass
    approve_or_reject(request,context)
    if 'action_success' not in context:
        get_pending_applications(context)
    return render(request,'review.html',context=context)

def officialLoggedInView(request):
    context = {}
    basic_functions(request,context)
    only_official(request,context)
    return render(request,'officialloggedin.html',context=context)

def electionPortalView(request):
    context = {}
    basic_functions(request,context)
    only_official(request,context)
    if 'success' not in context:
        vote(request,context)
        if 'check' in request.POST:
            get_approved_application(request.POST['aadhar'],context)
    return render(request,'electionportal.html',context=context)

def dashboardView(request):
    context = {}
    basic_functions(request,context)
    only_authenticated(request,context)
    try:
        role = user_role.objects.get(user=request.user).management_role
        if role == True:
            context['official'] = True
        else:
            context['user'] = True
    except:
        pass
    return render(request,'dashboard.html',context=context)