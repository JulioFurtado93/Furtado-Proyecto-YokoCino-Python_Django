from django.http import HttpResponse
from django.shortcuts import render
from YokoCino.models import *
from YokoCino.forms import *

# Create your views here.

def inicio(request):
    return render(request, "YokoCino/inicio.html")

def blog(request):
    return render(request, "YokoCino/blog.html")