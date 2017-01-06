from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Icon(models.Model):
    icon = models.ImageField(upload_to='images/icons', default='images/services/None/no-img.jpg')
    css = models.CharField(max_length=20)

    def __str__(self):
        return self.icon.url


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    url = models.URLField("Website", blank=True)
    profile_image = models.ImageField(upload_to='images/profile', default='images/profile/None/no-img.jpg')
    company = models.CharField(max_length=50, blank=True)
    intro = models.TextField()

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    profile = models.ForeignKey(UserProfile,related_name='contacts')
    phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    
    def __str__(self):
        return str(self.email+' '+self.phone+' for '+self.profile)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class SiteInfo(models.Model):
    profile = models.ForeignKey(UserProfile)


class Location(models.Model):
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    profile = models.OneToOneField(UserProfile, related_name='location')

    def __str__(self):
        return self.profile+' at '+str(self.latitude) + ' ' + str(self.longitude)


class Technology(models.Model):
    name = models.CharField(max_length=40)
    experience = models.PositiveIntegerField(default=1)
    knower = models.ForeignKey(SiteInfo, related_name='technologies')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    p_url = models.URLField("project_url", blank=True)
    s_url = models.URLField("source_url", blank=True)
    screenshot = models.ImageField(upload_to='images/projects', default='images/projects/None/no-img.jpg')
    technologies = models.ManyToManyField(Technology)
    owner = models.ForeignKey(SiteInfo, related_name='projects')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=30)
    icon = models.ForeignKey(Icon)
    url = models.URLField("service_link", blank=True)
    username = models.CharField(blank=True, max_length=20)
    user = models.ForeignKey(SiteInfo, related_name='services')

    def __str__(self):
        return self.name


class Message(models.Model):
    owner = models.ForeignKey(User)
    sender_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.sender_name+' to '+self.owner+': '+self.message
