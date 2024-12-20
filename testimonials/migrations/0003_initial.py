# Generated by Django 5.1.4 on 2024-12-20 16:10

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testimonials', '0002_delete_testimonial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author_name', models.CharField(default='Anonymous', max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('user_info', models.CharField(default='Enthusiast user', max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('body', models.TextField(validators=[django.core.validators.MinLengthValidator(20)])),
                ('approved', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]