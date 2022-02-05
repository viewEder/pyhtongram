from tabnanny import verbose
from django.db import models
from django.db.models import CASCADE    # Con esto administramos el comportamiento de las llaves foraneas
# importar el modelo de datos del usuario:
from django.contrib.auth.models import User

# Create your models here.

class Hilos(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True) 

    class Meta:
        verbose_name_plural = 'Hilos'

    def __str__(self) -> str:
        return self.usuario

class MensajesHilos(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    hilo = models.ForeignKey(Hilos, on_delete=CASCADE)
    # mensaje =
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True) 

    class Meta:
        verbose_name_plural = 'Mensajes'

    def __str__(self) -> str:
        return self.usuario, self.hilo

