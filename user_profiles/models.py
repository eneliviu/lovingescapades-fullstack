from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    '''
    User profile
    '''
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True
    )
    profile_name = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    # image = models.ImageField(
    #     upload_to='images/',
    #     # default="res.cloudinary.com/dchoskzxj/image/upload/v1734277998/tsipho0ghipyymo9gs9s_veaxrw.webp",
    #     default="../tsipho0ghipyymo9gs9s_veaxrw",
    #     blank=True
    # )
    image = CloudinaryField('image',
                            default="https://res.cloudinary.com/dchoskzxj/image/upload/v1728654902/df0u5irtlmygzx4frtfe.webp")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


# Create user profile when a new user registers
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)


# class Testimonial(models.Model):
#     '''
#     Stores a single testimonial text
#     '''
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE,
#                              related_name='testimonials')
#     author_name = models.CharField(
#         max_length=50,
#         blank=False,
#         default="Anonymous",
#         validators=[MinLengthValidator(2)]
#         )
#     user_info = models.CharField(
#         max_length=50,
#         blank=False,
#         default="Enthusiast user",
#         validators=[MinLengthValidator(2)]
#         )
#     body = models.TextField(
#         blank=False,
#         validators=[MinLengthValidator(20)]
#         )
#     created_at = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.author_name}'s testimonial"