# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Users is a model to represent the system's users
class Users(models.Model):
    ID_CHOICES = (('CC', 'Cedula de ciudadania'), ('TI', 'Tarjeta de identidad'), ('CE', 'Cedula de extranjería'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_id = models.CharField(max_length=30, verbose_name="type_id", choices=ID_CHOICES)
    id_number = models.CharField(max_length=30, verbose_name="identification")
    picture = models.ImageField(upload_to='images/')

