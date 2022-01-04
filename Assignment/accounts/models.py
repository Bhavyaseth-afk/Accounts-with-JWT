from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100 , unique=True)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    