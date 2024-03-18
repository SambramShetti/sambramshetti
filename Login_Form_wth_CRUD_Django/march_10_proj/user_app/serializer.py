from rest_framework import serializers
from user_app.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url = True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'image']
