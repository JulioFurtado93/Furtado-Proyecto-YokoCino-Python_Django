from django.urls import path
from Accounts.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_request, name='Login'),
    path('register', register, name='Register'),
    path('logout', LogoutView.as_view(template_name='Accounts/logout.html'), name='Logout'),
]