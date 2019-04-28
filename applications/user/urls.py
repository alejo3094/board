# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .views import Users

app_name="user_app"
urlpatterns = [
    url(r'^register/$',Users.as_view(), name='register'),
]