# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Users is a model to represent the system's users
class Users(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=30, verbose_name="identification")
    photo = models.ImageField(upload_to='images/', blank=True, null=True)