from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class ProfilForm(UserCreationForm): 
    email = models.EmailField(unique=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MessageForm(forms.ModelForm):
    pass