from django.urls import path
from Accounts.views import *
#from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('register/', register, name='Register'),
    path('logout/', logout_request, name='Logout'),
    path('profileEdit/', profileEdit, name='ProfileEdit'),
    path('addAvatar/', addAvatar, name='addAvatar'),
]