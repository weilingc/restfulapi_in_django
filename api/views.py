from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import models
from django.http import FileResponse


def uploadFile(request):
    if request.method == "POST":
        uploadedFile = request.FILES["uploadedFile"]

        # ORM把檔案存到後台
        document = models.Document(
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "upload-file.html", context = {
        "files": documents
    })
