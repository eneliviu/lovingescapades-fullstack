# Generated by Django 5.1.4 on 2024-12-15 15:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='tsipho0ghipyymo9gs9s_veaxrw'),
        ),
    ]
