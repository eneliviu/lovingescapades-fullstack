# Generated by Django 5.1.4 on 2024-12-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0003_rename_following_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../uqelsnhszwge3otibbsb', upload_to='images/'),
        ),
    ]
