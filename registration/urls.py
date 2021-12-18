from django.urls import path
from .views import ProfileUpdate

urlpatterns = [
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
