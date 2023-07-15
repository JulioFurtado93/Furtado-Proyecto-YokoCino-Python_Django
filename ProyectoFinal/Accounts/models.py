from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
class UserLink(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripcion',max_length=100,null=True, blank=True)
    link = models.URLField('Link',null=True, blank=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()