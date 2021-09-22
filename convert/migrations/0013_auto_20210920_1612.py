# Generated by Django 3.1.7 on 2021-09-20 15:12

import convert.formatChecker
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert', '0012_auto_20210918_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', convert.formatChecker.ContentTypeRestrictedFileField(blank=True, default='file', null=True, upload_to='', verbose_name='')),
            ],
        ),
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]
