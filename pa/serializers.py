from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    #full_name = Field(source='company')
    class Meta:
        model = UserProfile
        fields = ('__all__')
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(source="user_profile", read_only=True)
    
    class Meta:
        model = User
        fields = ('username','url','email','profile')



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        