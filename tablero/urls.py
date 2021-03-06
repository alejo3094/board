
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from tablero import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('applications.user.urls',namespace='users')),
    url(r'^', include('applications.board.urls',namespace='board')),
    url(r'^', include('applications.authentication.urls',namespace='authentication')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
