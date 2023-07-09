from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1000)
    author = models.CharField(max_length=40)
    fecha = models.DateField()
    #imagen