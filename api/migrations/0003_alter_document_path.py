# Generated by Django 4.0.5 on 2022-06-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_document_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(max_length=500),
        ),
    ]
