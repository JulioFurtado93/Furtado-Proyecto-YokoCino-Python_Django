from django.urls import path
from YokoCino.views import *

urlpatterns = [
    path('inicio/', inicio),
    path('blog/', blog, name="Blog"),
]