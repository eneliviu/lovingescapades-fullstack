from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from cloudinary.models import CloudinaryField
# from .user_profile.models import Profile
from .utils import get_coordinates


class Trip(models.Model):
    '''
    Trip model
    '''
    TRIP_CATEGORY = (('Leisure', 'LEISURE'),
                     ('Business', 'BUSINESS'),
                     ('Adventure', 'ADVENTURE'),
                     ('Family', 'FAMILY'),
                     ('Romantic', 'ROMANTIC'))
    TRIP_STATUS = (("Completed", 'COMPLETED'),
                   ("Ongoing", "ONGOING"),
                   ("Planned", 'PLANNED'))
    SHARE_CHOICES = (("Yes", "YES"),
                     ("NO", 'No'))

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='trips'
    )

    place = models.CharField(
        max_length=100,
        blank=False,
        validators=[MinLengthValidator(2)]
        )
    country = models.CharField(
        max_length=100,
        blank=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(56)
            ]
        )
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    trip_category = models.CharField(
        max_length=50,
        choices=TRIP_CATEGORY,
        default='LEISURE'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    trip_status = models.CharField(
        choices=TRIP_STATUS,
        default='PLANNED',
        max_length=50
    )
    shared = models.CharField(
        max_length=3,
        choices=SHARE_CHOICES,
        default='YES'
    )

    image = CloudinaryField('image', default=None, blank=True)
    coordinates = models.CharField(
        max_length=100,
        blank=True
    )

    # Raise Validation Error In Model Save Method:
    # https://ilovedjango.com/django/models-and-databases/tips/sub/raise-validation-error-in-model-save-method/

    is_cleaned = False

    def clean(self):
        self.is_cleaned = True
        coords = get_coordinates(self.place)

        if coords == 'location-error':
            raise ValidationError("Error: could not geocode the location")
        else:
            self.lat = coords[0]
            self.lon = coords[1]
        super(Trip, self).clean()

    def save(self, *args, **kwargs):
        '''
        Override the save() method to set the Lat and Lon values
        before saving.
        '''
        if not self.is_cleaned:
            self.full_clean()
        super(Trip, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.trip_category} trip to {self.place}, {self.country}'

    class Meta:
        ordering = ["-created_on", 'country', 'start_date']


class Image(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='images'
    )
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='images')
    # image = models.ImageField(upload_to='images/')
    title = models.CharField(
        max_length=50,
        blank=False,
        validators=[MinLengthValidator(2)])
    image = CloudinaryField(
        'image',
        default=None,
        blank=False
    )
    description = models.TextField(
        blank=False,
        validators=[
            MinLengthValidator(2),
            MaxLengthValidator(500)
            ]
        )
    shared = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo for {self.trip.title}, {self.trip.place},\
                 {self.trip.country}'

    class Meta:
        ordering = ["-uploaded_at"]
