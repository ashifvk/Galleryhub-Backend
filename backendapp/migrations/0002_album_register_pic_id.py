# Generated by Django 4.2.4 on 2023-10-15 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='gallery/')),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='pic_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backendapp.album'),
            preserve_default=False,
        ),
    ]