# -*- encoding: utf-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .views import index,registerPage
app_name="auth_app"
urlpatterns = [
    url('^$', index.as_view(), name='index'),
    url(r'^login/$', index.as_view(), name='login'),
    url(r'^register/$', registerPage.as_view(), name='register'),
]