from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    firstname = models.CharField(max_length=100, blank = True)
    lastname = models.CharField(max_length=100, blank = True)
    bio = models.TextField(blank = True)

    def __str__(self):
         return self.username
    
    class Meta: 
         ordering = ['lastname']

    def get_absolute_url(self):
         return reverse('user-detail', args=[str(self.id)]) 