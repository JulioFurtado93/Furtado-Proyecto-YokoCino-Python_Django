from django.http import HttpResponse
from django.shortcuts import render
from YokoCino.models import *
from Accounts.models import *
from YokoCino.forms import *

# Create your views here.

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "YokoCino/inicio.html", {'url':avatares[0].imagen.url})

def home(request):
    return render(request, "YokoCino/home.html")

def blog(request):
    return render(request, "YokoCino/blog.html")

def about(request):
    return render(request, "YokoCino/about.html")