# Generated by Django 4.0.5 on 2022-06-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_document_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='dateTimeOfUpload',
        ),
        migrations.RemoveField(
            model_name='document',
            name='path',
        ),
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]