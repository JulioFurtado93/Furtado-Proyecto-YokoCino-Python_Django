#from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from YokoCino.models import *
from Accounts.models import *
from YokoCino.forms import *
#from Accounts.views import getavatar
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.

def inicio(request):
    busqueda = request.GET.get('buscar')
    staff_group = get_object_or_404(Group, name='Staff')
    if busqueda:
        posts = Post.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(descripcion__icontains = busqueda),
            estado = True,
        ).distinct()
        pass
    else:
        posts = Post.objects.filter(estado = True)
        pass
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'YokoCino/inicio.html',{'posts':posts,'staff_group': staff_group})

def home(request):
    return render(request, "YokoCino/home.html")

def about(request):
    return render(request, "YokoCino/about.html")

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

@login_required
def setPost(request):
    if request.method == 'POST':
        miFormulario = formSetPost(request.POST, request.FILES)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            post = Post(
                titulo=data["titulo"],
                slug=data["slug"],
                descripcion=data["descripcion"],
                contenido=data["contenido"],
                imagen=request.FILES["imagen"],
                autor=data["autor"],
                categoria=data["categoria"],
                estado=data["estado"])    
            post.save()
            return render(request,"YokoCino/inicio.html")    
    else:
        miFormulario = formSetPost()
    return render(request, "YokoCino/setPost.html", {"miFormulario":miFormulario})

@login_required
def setCategoria(request):
    if request.method == 'POST':
        miFormulario = formSetCategoria(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            categoria = Categoria(
                nombre=data["nombre"],
                estado=data["estado"])    
            categoria.save()
            return render(request,"YokoCino/inicio.html")
    else:
        miFormulario = formSetCategoria()
    return render(request, "YokoCino/setCategoria.html", {"miFormulario":miFormulario})

@login_required
def setAutor(request):
    if request.method == 'POST':
        miFormulario = formSetAutor(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            autor = Autor(
                nombre=data["nombre"],
                apellido=data["apellido"],
                link=data["link"],
                email=data["email"],
                estado=data["estado"])    
            autor.save()
            return render(request,"YokoCino/inicio.html")
    else:
        miFormulario = formSetAutor()
    return render(request, "YokoCino/setAutor.html", {"miFormulario":miFormulario})

@login_required
def editPost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        miFormulario = formSetPost(request.POST, request.FILES, instance=post)
        if miFormulario.is_valid():
            miFormulario.save()
            return redirect('detalle_post', slug=post.slug)
    else:
        miFormulario = formSetPost(instance=post)
    return render(request, 'YokoCino/editPost.html', {'miFormulario': miFormulario, 'post': post})