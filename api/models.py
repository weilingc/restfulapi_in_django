from django.db import models

# Create your models here.

class Document(models.Model):
    uploadedFile = models.FileField(upload_to = "UploadedFiles/")

