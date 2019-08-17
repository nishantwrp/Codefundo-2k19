from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
from app import api
from app import mail

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
            logout(request)
            return "invalid_credentials"
    else:
        return "invaid_credentials"

def basic_functions(request,context):
    try:
        if request.GET['logout'] == 'true':
            logout(request)
            context['success'] = True
    except:
        pass

def only_unauthenticated(request,context):
    if request.user.is_authenticated:
        context['success'] = True

def only_authenticated(request,context):
    if not request.user.is_authenticated:
        context['success'] = True

def only_user(request,context):
    if not request.user.is_authenticated:
        context['success'] = True
    else:
        role = user_role.objects.get(user=request.user).management_role
        if role == True:
            context['success'] = True

def only_official(request,context):
    if not request.user.is_authenticated:
        context['success'] = True
    else:
        role = user_role.objects.get(user=request.user).management_role
        if role == False:
            context['success'] = True

def application_form_submit(request,context,fathers_name,address,pincode,dob,mobile,aadhar):
    try:
        x = application.objects.get(applicant=request.user)
        context['already_created_error'] = True
        return
    except:
        pass
    try:
        x = application.objects.get(aadhar=aadhar)
        context['already_created_error'] = True
        return
    except:
        pass
    r = api.submit_application(aadhar)
    application.objects.create(applicant=request.user,aadhar=aadhar,fathers_name=fathers_name,address=address,pincode=pincode,dob=dob,mobile=mobile,contract_id=r)
    context['submitted'] = True

def get_pending_applications(context):
    contracts = api.get_applications()['contracts']
    pending_applications_id = list()
    for contract in contracts:
        if contract['contractProperties'][0]['value'] == '0':
            pending_applications_id.append(contract['id'])
    pending_applications = list()
    for obj in pending_applications_id:
        application_data = {}
        x = application.objects.get(contract_id = obj)
        application_data['id'] = x.id
        application_data['aadhar'] = x.aadhar
        application_data['name'] = x.applicant.first_name + " " + x.applicant.last_name
        application_data['fathers_name'] = x.fathers_name
        application_data['dob'] = x.dob
        application_data['address'] = x.address
        application_data['pincode'] = x.pincode
        application_data['mobile'] = x.mobile
        application_data['status'] = "Pending"
        pending_applications.append(application_data)
    context['applications'] = pending_applications

def check_notapproved(a_id):
    x = application.objects.get(id=a_id)
    if x.approved == False:
        return True
    else:
        return False

def approve_or_reject(request,context):
    if 'approve' in request.GET:
        a_id = request.GET['approve']
        if check_notapproved(a_id):
            contract_id = application.objects.get(id=a_id).contract_id
            api.application_action(contract_id,'approve')
            x = application.objects.get(id=a_id)
            x.approved = True
            x.save()
            mail.send_email(application.objects.get(id=a_id).applicant.username,"Your VoterId Application With Aadhar " + application.objects.get(id=a_id).aadhar + " Has Been Approved.","LetsVote Application Approved")
            context['action_success'] = True
    elif 'reject' in request.GET:
        a_id = request.GET['reject']
        if check_notapproved(a_id):
            contract_id = application.objects.get(id=a_id).contract_id
            api.application_action(contract_id,'reject')
            mail.send_email(application.objects.get(id=a_id).applicant.username,"Your VoterId Application With Aadhar " + application.objects.get(id=a_id).aadhar  + " Has Been Rejected. Please Try Submitting Your Application Again.","LetsVote Application Rejected")
            application.objects.filter(id=a_id).delete()
            context['action_success'] = True

