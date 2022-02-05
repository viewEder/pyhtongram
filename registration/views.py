from django import dispatch
from django import forms
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
# Cargar el formulario de creación de usuarios:
from django.contrib.auth.forms import UserCreationForm
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
class RegistroView(CreateView):
    # Damos uso del formulario existente de django.
    form_class = UserCreationForm
    template_name = 'registration/registro.html'

    def get_success_url(self):
        return reverse_lazy('login')

    def get_form(self, form_class=None):
        form = super(RegistroView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs = {'class':'form-control mb-1', 'placeholder':'NickName de Usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs = {'class':'form-control mb-1', 'placeholder':'Password de Usuario'})
        form.fields['password2'].widget = forms.PasswordInput(attrs = {'class':'form-control mb-1', 'placeholder':'Confirmar Password de Usuario'})
        
        return  form

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