# Generated by Django 5.1.4 on 2024-12-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0028_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../tsipho0ghipyymo9gs9s_veaxrw', upload_to='images/'),
        ),
    ]
