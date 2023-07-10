from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from YokoCino.models import *
from Accounts.models import *
from YokoCino.forms import *
from Accounts.views import getavatar
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    avatar = getavatar(request)
    return render(request, "YokoCino/inicio.html", {"avatar":avatar})

def home(request):
    publicaciones = Blog.objects.all()
    return render(request, "YokoCino/home.html", {'publicaciones':publicaciones})

def blog(request):
    publicaciones = Blog.objects.all()
    return render(request, "YokoCino/blog.html", {'publicaciones':publicaciones})

@login_required
def setEntry(request):
    if request.method == 'POST':
        miFormulario = formSetBlog(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            entry = Blog(title=data["title"],subtitle=data["subtitle"],cuerpo=data["cuerpo"],author=data["author"],fecha=data["fecha"])    
            entry.save()
            return render(request,"YokoCino/home.html")    
    else:
        miFormulario = formSetBlog()
    return render(request, "YokoCino/setEntry.html", {"miFormulario":miFormulario})

def getEntry(request):
    return render(request, "YokoCino/getEntry.html")

def searchEntry(request):
    if request.GET["title"]:
        title = request.GET["title"]
        entries = Blog.objects.filter(title = title)
        return render(request, "YokoCino/getEntry.html", {"entries":entries})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Blog, pk=pk)
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})

def about(request):
    return render(request, "YokoCino/about.html")