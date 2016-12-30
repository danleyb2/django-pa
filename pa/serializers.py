from django.forms import widgets
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model=Icon 
        fields = ('__all__')
    
class ServiceSerializer(serializers.ModelSerializer):
    icon=IconSerializer()
    class Meta:
        model = Service
        fields = ('__all__')

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('__all__')

class TechnologyNameSerializer(TechnologySerializer):
    class Meta:
        model = Technology
        fields = ('name')

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = ('__all__')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude','longitude',)
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')
        
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    #full_name = Field(source='company')
    info = serializers.SerializerMethodField()
    contact = ContactSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    #profile_image_url = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = UserProfile
        fields = ('location', 'info','contact')
    
    def get_image_url(self,user_profile):
        return user_profile.profile_image.url
        
    def get_info(self,user_profile):
        return dict(
            first_name=user_profile.user.first_name,
            last_name=user_profile.user.last_name,
            icon=self.context['request'].build_absolute_uri(user_profile.profile_image.url),
            email=user_profile.user.email,
            about=user_profile.intro,
            company=user_profile.company,
            website=user_profile.url
            )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(source="user_profile", read_only=True)
    name = serializers.SerializerMethodField('full_name')
    
    class Meta:
        model = User
        fields = ('name','first_name','last_name','username','url','email','profile')

    def full_name(self,user):
        return user.first_name+' '+user.last_name

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class SiteSerializer(serializers.HyperlinkedModelSerializer):
    
    profile = UserProfileSerializer()
    technologies = TechnologySerializer(read_only=True,many=True)
    projects = ProjectSerializer(read_only=True,many=True)
    services = ServiceSerializer(read_only=True,many=True)
    #profile_image_url = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = SiteInfo
        fields = ('profile','technologies','projects','services')
    
    def get_image_url(self,user_profile):
        return user_profile.profile_image.url
        
    def get_profile_info(self,user_p):
        return dict(
            location = LocationSerializer(read_only=True)
            )
   
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')