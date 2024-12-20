from django.db.models import Count
from rest_framework import generics
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TestimonialSerializer
from .models import Testimonial
from user_profiles.models import Profile
from backend.permissions import IsOwnerOrReadOnly


class TestimonialList(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # dynamic ordering based on fields
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]


class TestimonialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

