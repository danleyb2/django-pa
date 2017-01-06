from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from .models import UserProfile,SiteInfo
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions


# Create your views here.

def save_profile():
    user = User.objects.create_user('bob', 'bob@example.com', 'password')
    user.first_name = "Bob"
    user.last_name = "Smith"
    user.save()
    
    user_profile = user.get_profile()
    user_profile.display_name = "Bob Smith"
    user_profile.save()

@login_required
def index(request):
    user_profile = request.user.profile
    
    return HttpResponse("User url is : "+user_profile.url)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class MessageSendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['post']


class MessagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get']


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows location to be updated.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['post']
    
    #def get_serializer_context(self):
    #    return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class SiteDataViewSet(viewsets.ModelViewSet):
    '''
    retrieve complete site info
    '''
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SiteInfo.objects.all()
    serializer_class = SiteSerializer
    
    
    def get_serializer_context(self):
        return {'request': self.request}
    
