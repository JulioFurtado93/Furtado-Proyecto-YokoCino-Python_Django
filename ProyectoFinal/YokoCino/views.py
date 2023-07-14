from django.http import HttpResponse
from django.shortcuts import render
from YokoCino.models import *
from Accounts.models import *
from YokoCino.forms import *
#from Accounts.views import getavatar
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

def inicio(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        posts = Post.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(descripcion__icontains = busqueda),
            estado = True,
        ).distinct()
    else:
        posts = Post.objects.filter(estado = True)
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'YokoCino/inicio.html',{'posts':posts})

def about(request):
    return render(request, "YokoCino/about.html")

#def inicio(request):
#    avatar_url = getavatar(request)
#    print (avatar_url)
#    return render(request, "YokoCino/inicio.html", {"avatar_url":avatar_url})

#def home(request):
#    publicaciones = Blog.objects.all()
#    return render(request, "YokoCino/home.html", {'publicaciones':publicaciones})

def ensaladas(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = 'Ensaladas')
    )
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'YokoCino/ensaladas.html',{'posts':posts})

def carnes(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = 'Carnes')
    )
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'YokoCino/carnes.html',{'posts':posts})

def guisos(request):
    posts = Post.objects.filter(
        estado = True, 
        categoria = Categoria.objects.get(nombre = 'Guisos')
    )
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'YokoCino/guisos.html',{'posts':posts})

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    return render(request,'YokoCino/post.html',{'detalle_post':post})

#def blog(request):
#    publicaciones = Blog.objects.all()
#    return render(request, "YokoCino/blog.html", {'publicaciones':publicaciones})

#@login_required
#def setEntry(request):
#    if request.method == 'POST':
#        miFormulario = formSetBlog(request.POST)
#        print(miFormulario)
#        if miFormulario.is_valid:
#            data = miFormulario.cleaned_data
#            entry = Blog(title=data["title"],subtitle=data["subtitle"],cuerpo=data["cuerpo"],author=data["author"],fecha=data["fecha"])    
#            entry.save()
#            return render(request,"YokoCino/home.html")    
#    else:
#        miFormulario = formSetBlog()
#    return render(request, "YokoCino/setEntry.html", {"miFormulario":miFormulario})
#
#def getEntry(request):
#    return render(request, "YokoCino/getEntry.html")
#
#def searchEntry(request):
#    if request.GET["title"]:
#        title = request.GET["title"]
#        entries = Blog.objects.filter(title = title)
#        return render(request, "YokoCino/getEntry.html", {"entries":entries})
#    else:
#        respuesta = "No se enviaron datos"
#    return HttpResponse(respuesta)

#def detalle_publicacion(request, pk):
#    publicacion = get_object_or_404(Blog, pk=pk)
#    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})


