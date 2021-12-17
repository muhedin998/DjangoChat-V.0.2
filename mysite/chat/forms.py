from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from .models import Profil

class ProfilForm(UserCreationForm): 
    email = models.EmailField(unique=True)
    class Meta:
        model = Profil
        fields = ['username','email','password1','password2']
    