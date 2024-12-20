from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.permissions import IsOwnerOrReadOnly
from .models import Trip, Image
from .serializers import TripSerializer, ImageSerializer


# Create your views here.
class TripList(generics.ListCreateAPIView):
    '''
    List all trips or create a new trip.
    '''
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # dynamic ordering based on fields
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    # `filterset_fields` for advanced filtering through complex
    # relationship pathways
    # filterset_fields = [
    #     'owner__follows__followed_by__profile',
    #     'owner__followed_by__owner__profile',
    # ]

    ordering_fields = [
        'owner',
        'title',
        'created_at',
        'updated_at',
    ]

    def get_queryset(self):
        # add additional computed fields in the query
        queryset = Trip.objects.order_by('-created_on')

        # Additional filtering logic (if needed)
        owner_username = self.request.query_params.get('owner__username', None)
        if owner_username:
            queryset = queryset.filter(owner__username=owner_username)

        return queryset


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete a trip instance.
    '''
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ImageList(generics.ListCreateAPIView):
    '''
    List all images or create a new image.
    '''
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnly]  # [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['uploaded_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # add additional computed fields in the query
        queryset = Image.objects.order_by('-uploaded_at')

        # Additional filtering logic (if needed)
        owner_username = self.request.query_params.get('owner__username', None)
        if owner_username:
            queryset = queryset.filter(owner__username=owner_username)

        return queryset


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, update or delete an image instance.
    '''
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnly]
