from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator


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
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


# Create user profile when a new user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    Create profile for new user automatically
    '''
    if created:
        user_profile = Profile(owner=instance)
        user_profile.save()
        # User follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


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