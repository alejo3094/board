# -*- encoding: utf-8 -*-

from django.conf.urls import url

from .views import dashBoard
app_name="auth_app"
urlpatterns = [
    url('^$', dashBoard.as_view(), name='index'),
    url(r'^dashBoard/$', dashBoard.as_view(), name='register'),
]