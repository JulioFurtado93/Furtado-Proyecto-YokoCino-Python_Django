from django.urls import path
from YokoCino.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='Home'),
    path('inicio/', inicio, name='Inicio'),
    path('blog/', blog, name='Blog'),
    path('setEntry/', setEntry, name="setEntry"),
    path('getEntry/', getEntry, name="getEntry"),
    path('searchEntry/', searchEntry, name="searchEntry"),
    path('about/', about, name='About'),
    path('publicacion/<int:pk>/', detalle_publicacion, name='detalle_publicacion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)