# Generated by Django 4.2.4 on 2023-10-12 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('log_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.login')),
            ],
        ),
    ]
