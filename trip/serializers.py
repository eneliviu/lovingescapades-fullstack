from rest_framework import serializers
from .models import Trip, Image


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        # fields = '__all__'
        fields = [
            'id', 'owner', 'trip', 'title', 'image',
            'description', 'shared', 'uploaded_at'
        ]
