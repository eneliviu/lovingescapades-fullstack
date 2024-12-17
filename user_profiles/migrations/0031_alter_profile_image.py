# Generated by Django 5.1.4 on 2024-12-16 16:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0030_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dchoskzxj/image/upload/v1734277998/tsipho0ghipyymo9gs9s_veaxrw.webp', max_length=255, verbose_name='tsipho0ghipyymo9gs9s_veaxrw'),
        ),
    ]
