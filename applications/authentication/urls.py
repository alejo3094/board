# -*- encoding: utf-8 -*-

from django.conf.urls import url
from .views import login,registerPage
app_name="auth_app"
urlpatterns = [

    url(r'^login/$', login.as_view(), name='login'),
    url(r'^register/$', registerPage.as_view(), name='register'),
]