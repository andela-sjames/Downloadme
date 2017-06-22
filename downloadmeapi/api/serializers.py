from rest_framework import serializers

from django.contriber.auth.models import User

from .models import Download


class DownloadSerializer(serializers.ModelSerializer):
    
    class Meta:
        Model = Download
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')

    