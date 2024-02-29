from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['id', 'user_name', 'user_phone', 'user_email', 'location']