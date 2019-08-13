from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def userloginView(request):
    return render(request,'userlogin.html')

def userLoggedInView(request):
    return render(request,'userloggedin.html')