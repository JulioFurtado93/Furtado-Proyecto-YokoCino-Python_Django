from django.urls import path
from YokoCino.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name= 'Inicio'),
    path('inicio/', inicio, name='Inicio'),
    #path('blog/', blog, name='Blog'),
    #path('setEntry/', setEntry, name="setEntry"),
    #path('getEntry/', getEntry, name="getEntry"),
    #path('searchEntry/', searchEntry, name="searchEntry"),
    path('ensaladas/', ensaladas, name = 'Ensaladas'),
    path('carnes/', carnes, name = 'Carnes'),
    path('guisos/', guisos, name = 'Guisos'),
    path('about/', about, name='About'),
    path('<slug:slug>/',detallePost, name = 'detalle_post'),
    #path('publicacion/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)