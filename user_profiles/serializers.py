from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Fields:
    - `owner`: A `ReadOnlyField` that accesses and serializes
        the `username` of the profile's owner.
    - `is_owner`: A `SerializerMethodField` that determines
        whether the current request's user is the owner of the
        profile, facilitating client-side authorization logic.
    - `following_id`: Another `SerializerMethodField` that returns
        the ID of the `Follower` relation
        if the current user follows the profile's owner.
    - `posts_count`, `followers_count`, `following_count`: Read-only fields,
        likely computed elsewhere, to provide aggregated data about posts,
        followers, and followings related to the profile.

    Methods:
    - `get_is_owner(self, obj)`: Checks if the user making the request is
        the owner of the profile.
    - `get_following_id(self, obj)`: Returns the ID of the following
        relationship if the requesting user is authenticated and follows
        the profile owner.

    Meta Class:
    - The `Meta` class specifies the model (`Profile`) and fields that should
        be included in the serialized output.
    '''
    owner_username = serializers.ReadOnlyField(source='owner.username')
    is_following = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    # Adding annotated fields
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'owner_username', 'profile_name', 'content',
            'image', 'created_at', 'updated_at', 'follows',
            'followers_count', 'following_count',
            'is_following', 'is_owner'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def get_is_following(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.followed_by.filter(id=request.user.profile.id).exists()
        return False

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.owner == request.user
        return False
