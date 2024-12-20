from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
