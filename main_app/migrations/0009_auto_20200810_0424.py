# Generated by Django 3.1 on 2020-08-10 04:24

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200809_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='upload_picture',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/uploads/', location='/Users/briansanchez/sei/unit-3/projects/theSpot/media/uploads/'), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_picture',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/uploads/', location='/Users/briansanchez/sei/unit-3/projects/theSpot/media/uploads/'), upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='upload_picture',
            field=models.ImageField(blank=True, default='uploads/default_picture.png', null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/media/uploads/', location='/Users/briansanchez/sei/unit-3/projects/theSpot/media/uploads/'), upload_to='uploads/'),
        ),
    ]
