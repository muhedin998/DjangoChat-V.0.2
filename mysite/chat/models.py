from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django import forms

class Profil(User):
    def korisnik(self):
        return self.username