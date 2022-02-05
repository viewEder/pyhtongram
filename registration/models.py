from django.db import models
# El modelo de datos de usuario se encuentra en django:
from django.contrib.auth.models import User
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.forms import ClearableFileInput
# Importamos los seleccionables:
from core.types.generos import Generos
# Importamos decoradores de autenticacion:
from django.dispatch import receiver
from django.db.models.signals import post_save

# 6. Create your models here.

# Función para subir imagenes de perfil de usuario:
def subirPerfil(instance, filename):
    old_instance = ProfileModel.objects.get(pk = instance.pk)
    old_instance.avatar.delete()
    return 'perfiles/'+ filename

# Función para subir imagen de portada:
def subirPortada(instance, filename):
    old_instance = ProfileModel.objects.get(pk = instance.pk)
    old_instance.portada.delete()
    return 'portadas/'+ filename

class ProfileModel(models.Model):
    # Atributos propios de la clase:
    usuario = models.OneToOneField(User,on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = subirPerfil,  null = True, blank = True)
    portada = models.ImageField(upload_to = subirPortada, null = True, blank = True)
    presentacion = models.TextField(verbose_name = "Biografia", max_length = 1000, null = True, blank = True)
    genero = models.CharField(verbose_name = "Género", choices = Generos, null= False, max_length = 40)
    telefono = models.CharField(verbose_name= " Teléfono", null= True, blank= True, max_length=40)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null= True, auto_now=False, auto_now_add=False)
    link_url = models.URLField(max_length=250, null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True) 

    class Meta:
        ordering = ['usuario__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        ProfileModel.objects.get_or_create(usuario = instance)