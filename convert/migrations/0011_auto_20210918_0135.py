# Generated by Django 3.1.7 on 2021-09-18 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0010_fileupload_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='name',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='file',
            field=models.FileField(default='file', null=True, upload_to='', verbose_name=''),
        ),
    ]