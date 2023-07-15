from django.db import models

# Create your models here.
#class Blog(models.Model):
#    title = models.CharField(max_length=100)
#    subtitle = models.CharField(max_length=100)
#    cuerpo = models.TextField(max_length=1000)
#    author = models.CharField(max_length=40)
#    fecha = models.DateField()
#    imagen = models.ImageField(upload_to='blogimg', null=True, blank=True)
#
#    def __str__(self):
#        return self.title
    
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de categoría',max_length = 50, null= False, blank= False)
    estado = models.BooleanField('Categoría activada/Categoría desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now= False, auto_now_add= True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Autor',max_length = 50, null= False, blank= False)
    apellido = models.CharField('Apellido de Autor',max_length = 50, null= False, blank= False)
    link = models.URLField('Link', null = True, blank = True)
    email = models.EmailField ('Email', null = False, blank = False)
    estado = models.BooleanField('Autor activado/Autor desactivado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now= False, auto_now_add= True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    def __str__(self):
        return '{0},{1}'.format(self.apellido, self.nombre)
    
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo',max_length = 100, null= False, blank= False)
    slug = models.CharField('Slug',max_length = 100, null= False, blank= False)
    descripcion = models.CharField('Descripcion',max_length = 150, null= False, blank= False)
    contenido = models.TextField('Contenido')
    #imagen = models.URLField('Imagen',max_length = 255, null = False, blank = False)
    imagen = models.ImageField(upload_to='blogimg', null=True, blank=True)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add= True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo