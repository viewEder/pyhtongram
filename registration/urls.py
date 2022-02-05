from django.urls import path
from .views import ProfileUpdate, RegistroView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
