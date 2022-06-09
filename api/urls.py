from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "api"

urlpatterns = [
    path("", views.uploadFile, name = "uploadFile"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
