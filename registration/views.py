from django import dispatch
from django.shortcuts import render
from django.views.generic.edit import UpdateView
# Importamos los decoradores:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Importamos el router rápido:
from django.urls import reverse_lazy
# importar los formularios creados:
from .form import ProfileForm
# importamos el modelo de datos de profile:
from .models import ProfileModel

# Create your views here.
@method_decorator(login_required, name= 'dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Sobreescribimos el método get para traer los objetos del modelo de datos:
    def get_object(self):
        # Recuperamos el objeto usuario que se va a editar:
        profile, created = ProfileModel.objects.get_or_create(usuario = self.request.user)
        return profile