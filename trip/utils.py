from geopy import geocoders
from geopy.exc import GeocoderTimedOut


def get_coordinates(location, attempt=1, max_attempts=5):
    '''
    Geocodes an address with retry on timeout.
    GeoPy documentation:
    https://geopy.readthedocs.io/en/latest/#geopy.exc.GeocoderTimedOut

    Parameters:
    location (str): The location to geocode.
    attempts (int, optional): Current retry attempt. Default is 1.
    max_attempts (int, optional): Maximum retry attempts. Default is 5.

    Returns:
    tuple: Geocoded location data (Latitude and Longitude).

    Raises:
    GeocoderTimedOut: If the max number of attempts is exceeded.
    '''
    geocoder = geocoders.Nominatim(user_agent='trip')
    try:
        get_location = geocoder.geocode(location, exactly_one=True,
                                        language='en')

        if get_location:
            return get_location.latitude, get_location.longitude
        else:
            # raise ValueError("Could not geocode the location")
            return "location-error"
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            print(f"Attempt {attempt} failed; retrying...")
            return get_coordinates(location,
                                   attempt=attempt+1,
                                   max_attempts=max_attempts)
        # raise GeocoderTimedOut("Max attempts exceeded")
        return 'max-attempts-exceeded-error'


# class Activity(models.Model):
#     trip = models.ForeignKey(Trip,
#                              on_delete=models.CASCADE,
#                              related_name='activities')
#     name = models.CharField(max_length=255)

#     # Optional field,stored as an empty string if left blank
#     description = models.TextField(blank=True)
#     date = models.DateField()

#     class Meta:
#         verbose_name = 'Activity'
#         verbose_name_plural = 'Activity'

#     def __str__(self):
#         return self.name


# class AbstractPostModel(models.Model):
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE,
#                              related_name='%(class)ss')
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         abstract = True
#         ordering = ["-created_on"]  # descending order of creation date


# class Comment(AbstractPostModel):
#     COMMENT_STATUS = ((0, "Draft"),
#                       (1, "Published"))
#     trip = models.ForeignKey(Trip,
#                              on_delete=models.CASCADE,
#                              related_name='comments')
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f'Comment by {self.user.username} for \
#                             {self.trip.user} on \
#                             "{self.trip.title}" post'


# class Note(AbstractPostModel):
#     NOTE_STATUS = ((0, "Draft"),
#                    (1, "Published"))
#     trip = models.ForeignKey(Trip,
#                              on_delete=models.CASCADE,
#                              related_name='notes')
#     status = models.IntegerField(choices=NOTE_STATUS,
#                                  default=0)

#     def __str__(self):
#         return f'Post by {self.user.username} on {self.trip.title}'

# class About(models.Model):
#     """
#     Stores a single about me text
#     """
#     title = models.CharField(max_length=200)
#     profile_image = CloudinaryField('image', default='placeholder')
#     updated_on = models.DateTimeField(auto_now=True)
#     content = models.TextField()

#     def __str__(self):
#         return self.title


# class ContactUs(models.Model):
#     """
#     Stores a single collaboration request message
#     """
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     message = models.TextField()
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Collaboration request from {self.name}"