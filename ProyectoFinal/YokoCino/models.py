from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=1000)
    author = models.CharField(max_length=40)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='blogimg', null=True, blank=True)

    def __str__(self):
        return self.title