# Generated by Django 5.1.4 on 2024-12-20 15:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profiles', '0033_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(default='Anonymous', max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('user_info', models.CharField(default='Enthusiast user', max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('body', models.TextField(validators=[django.core.validators.MinLengthValidator(20)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='user_profiles.profile')),
            ],
        ),
    ]
