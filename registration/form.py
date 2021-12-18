# Cargar la clase form de django:
from django import forms
from django.db.models import fields
from django.forms import widgets    
# Cargar el modelo de datos:
from django.contrib.auth.models import User     # el modelo de datos de django 
from .models import ProfileModel                # Importamos la clase profilemodel creada en el archivo models.py

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['avatar','portada','presentacion','genero','telefono','fecha_nacimiento','link_url']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control mt-3 img-fluid'}),
            'portada': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'presentacion': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':'5'}),
            'genero': forms.Select(attrs={'class':'form-control mt-3'}),
            'telefono': forms.TextInput(attrs={'class':'form-control mt-3', 'type':'number'}),
            'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control mt-3', 'type':'date'}),
            'link_url': forms.URLInput(attrs={'class':'form-control mt-3'})
        }
