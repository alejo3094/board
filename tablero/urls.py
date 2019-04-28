
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('applications.user.urls',namespace='users')),
]
