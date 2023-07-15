from django import forms
from YokoCino.models import *

class formSetBlog(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)
    author = forms.CharField(max_length=40)
    fecha = forms.DateField()
    imagen = forms.ImageField()

class formSetPost(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'descripcion', 'contenido', 'imagen', 'autor', 'categoria', 'estado']