from django import forms
from YokoCino.models import *

class formSetPost(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'descripcion', 'contenido', 'imagen', 'autor', 'categoria', 'estado']

class formSetCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'estado']

class formSetAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'link', 'email', 'estado']