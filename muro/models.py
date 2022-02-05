from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Importamos decoradores de autenticacion:
from django.dispatch import receiver
from django.db.models.signals import post_save

# Función para subir fotos:
def subir_foto_user(instance, filename):
    path = 'usuarios/' + instance + filename
    return path 

# Create your models here.
class AlbumUsuario(models.Model):
    # Atributos del Muro y Album:
    usuario = models.ForeignKey(User, on_delete=CASCADE, verbose_name='usuario')
    nombre_foto = models.ImageField(upload_to = 'subir_foto_user', verbose_name='Foto')
    descripcion_foto = models.CharField(verbose_name='Descripción', max_length=255, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True) 

    class Meta:
        verbose_name_plural = 'Fotos de Usuarios'

    def __str__(self):
        return self.nombre_foto
    

@receiver(post_save, sender=User)
def ensure_album_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        AlbumUsuario.objects.get_or_create(usuario = instance)