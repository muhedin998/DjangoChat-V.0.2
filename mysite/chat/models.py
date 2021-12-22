from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django import forms

class Profil(User):
    def korisnik(self):
        return self.username

class Message(models.Model):
    sender = Profil
    content = models.TextField()
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender
    
    def poruka(self):
        return self.content