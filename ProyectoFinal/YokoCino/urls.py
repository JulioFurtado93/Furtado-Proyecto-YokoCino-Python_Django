from django.urls import path
from YokoCino.views import *

urlpatterns = [
    path('', home, name='Home'),
    path('inicio/', inicio, name='Inicio'),
    path('blog/', blog, name='Blog'),
    path('about/', about, name='About'),
]