from django.db import models

# Create your models here.
class Articulos(models.Model):
    nombre    = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio    = models.CharField(max_length=100)
    img       = models.ImageField(default='null', upload_to='ArtiguloIMG')
 
class PedidoDE(models.Model):
    
    nombreA    = models.CharField(max_length=100)
    precioA    = models.CharField(max_length=100)
    imgA       = models.ImageField(default='null', upload_to='ArtiguloIMG')

