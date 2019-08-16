from django.urls import path
from .views import *
urlpatterns = [
    path('',indexView),
    path('dashboard/user/',userLoggedInView),
    path('voterid/',voterIDView),
    path('login/user/',userloginView),
    path('login/gov/',govloginView),
    path('register/',registerView),
    path('search/',searchView),
    path('officialloggedin/',officialLoggedInView),
    path('electionportal/',electionPortalView),
    path('votedusers/',votedView),
    path('review/',reviewView),
]