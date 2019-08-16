from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request,'index.html')

def userloginView(request):
    return render(request,'userlogin.html')

def userLoggedInView(request):
    return render(request,'userloggedin.html')

def voterIDView(request):
    return render(request,'voterid.html')

def govloginView(request):
    return render(request,'govlogin.html')

def registerView(request):
    return render(request,'signup.html')

def searchView(request):
    return render(request,'search.html')

def votedView(request):
    return render(request,'votedusers.html')

def reviewView(request):
    return render(request,'review.html')
