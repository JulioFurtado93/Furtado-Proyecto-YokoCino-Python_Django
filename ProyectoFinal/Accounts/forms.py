from django import forms
from Accounts.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Modificar nombre')
    last_name = forms.CharField(label='Modificar apellido')
    descripcion = forms.CharField(label='Modificar descripción',max_length=100, required=False)
    link = forms.URLField(label='Link', required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'descripcion', 'link']

class AvatarForm(forms.Form):
    avatar = forms.ImageField()

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)

    class Meta:
        model = Message
        fields = ['recipient', 'content']