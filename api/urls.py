from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "api"

urlpatterns = [
    path("", views.uploadFile, name = "uploadFile"),
    # path('download_file/<id>', views.download_file, name = "download_file"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )
