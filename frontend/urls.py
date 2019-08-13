from django.urls import path
from .views import *
urlpatterns = [
    path('',indexView),
    path('login/',userloginView),
    path('userloggedin/',userLoggedInView),
    path('voterid/',voterIDView),
]