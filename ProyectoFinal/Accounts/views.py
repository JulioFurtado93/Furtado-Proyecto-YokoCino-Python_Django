from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm #UserCreationForm
from django.contrib.auth import login,logout,authenticate
from Accounts.forms import *
from Accounts.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def login_request(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'Accounts/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'Accounts/login.html')

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"YokoCino/inicio.html")
    else:
        #form = UserCreationForm()       
        form = UserRegisterForm()     
    return render(request,"Accounts/register.html" ,  {"form":form})

def logout_request(request):
    logout(request)
    return redirect(reverse('Inicio'))

@login_required  
def profile(request):
    avatar_url = getavatar(request)
    return render(request, 'Accounts/profile.html',{'usuario': request.user, 'avatar_url': avatar_url})

@login_required
def profileEdit(request):
    usuario = request.user
    avatar_url = getavatar(request)
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            user_link, _ = UserLink.objects.get_or_create(user=usuario)
            user_link.descripcion = informacion['descripcion']
            user_link.link = informacion['link']
            user_link.save()
            return render(request, "YokoCino/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "Accounts/profileEdit.html", {"miFormulario": miFormulario, "usuario": usuario,"avatar_url":avatar_url})

@login_required
def addAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarForm(request.POST, request.FILES)
        if miFormulario.is_valid:
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['avatar'])
            avatar.save()
            return render(request,"YokoCino/inicio.html")
    else:
        miFormulario = AvatarForm()
    return render(request,"Accounts/addAvatar.html",{'miFormulario':miFormulario})

def getavatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar:
        avatar_url = avatar.imagen.url
    else:
        avatar_url = None
    return avatar_url

@login_required
def sendMessage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return render(request,'YokoCino/inicio.html')
    else:
        form = MessageForm()    
    return render(request, 'Accounts/sendMessage.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'Accounts/inbox.html', {'messages': messages})

#def getavatar(request):
#    avatar = Avatar.objects.filter(user = request.user.id)
#    try:
#        avatar = avatar[0].image.url
#    except:
#        avatar = None
#    return avatar