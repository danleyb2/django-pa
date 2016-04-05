from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User ,related_name='user_profile')
    url = models.URLField("Website", blank=True)
    profile_image = models.ImageField(upload_to='images/profile',default = 'images/profile/None/no-img.jpg')
    company = models.CharField(max_length=50, blank=True)
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Technology(models.Model):
    name = models.CharField(max_length=40)
    experience = models.PositiveIntegerField(default=1)
    knower = models.ForeignKey(User)

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    p_url = models.URLField("project_url", blank=True)
    s_url = models.URLField("source_url", blank=True)
    screenshot = models.ImageField(upload_to='images/projects',default = 'images/projects/None/no-img.jpg')
    technologies = models.ManyToManyField(Technology)
    owner = models.ForeignKey(User)
    
    
class Service(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField("service_link", blank=True)
    username = models.CharField(blank=True,max_length=20)
    user = models.ForeignKey(User)
    
