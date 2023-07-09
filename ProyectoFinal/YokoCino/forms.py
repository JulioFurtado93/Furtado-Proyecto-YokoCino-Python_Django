from django import forms

class formSetBlog(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=1000)
    author = forms.CharField(max_length=40)
    fecha = forms.DateField()
    #imagen