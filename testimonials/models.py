from django.db import models
from django.core.validators import MinLengthValidator
# from user_profiles.models import Profile
from django.contrib.auth.models import User


class Testimonial(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # profile = models.ForeignKey(Profile,
    #                             on_delete=models.CASCADE,
    #                             related_name='testimonials')
    author_name = models.CharField(
        max_length=50,
        blank=False,
        default="Anonymous",
        validators=[MinLengthValidator(2)]
    )
    user_info = models.CharField(
        max_length=50,
        blank=False,
        default="Enthusiast user",
        validators=[MinLengthValidator(2)]
    )
    body = models.TextField(
        blank=False,
        validators=[MinLengthValidator(20)]
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author_name}'s testimonial"
