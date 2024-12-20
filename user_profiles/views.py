from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    '''
    List all profiles with aggregation fields for posts, followers,
    and following counts.
    No create view as profile creation is handled by Django signals.
    '''
    serializer_class = ProfileSerializer
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
        # 'posts_count',
        'followers_count',
        'following_count',
        'owner__follows__created_at',
        'owner__followed_by__created_at'
    ]

    def get_queryset(self):
        # add additional computed fields in the query
        queryset = Profile.objects.annotate(
            # posts_count=Count('owner__post', distinct=True),
            followers_count=Count('followed_by', distinct=True),
            following_count=Count('follows', distinct=True)
        ).order_by('-created_at')

        # Additional filtering logic (if needed)
        owner_username = self.request.query_params.get('owner__username', None)
        if owner_username:
            queryset = queryset.filter(owner__username=owner_username)

        return queryset


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        # posts_count=Count('owner__post', distinct=True),  # how many posts an user has using Count()
        followers_count=Count('followed_by', distinct=True),
        following_count=Count('follows', distinct=True)
    ).order_by('-created_at')
