from django.urls import path
from .views import *
urlpatterns = [
    path('',indexView),
    path('userloggedin/',userLoggedInView),
    path('voterid/',voterIDView),
    path('login/user/',userloginView),
    path('login/gov/',govloginView),
    path('register/',registerView),
]