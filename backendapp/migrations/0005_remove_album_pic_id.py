# Generated by Django 4.2.4 on 2023-10-15 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0004_album_pic_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='pic_id',
        ),
    ]
