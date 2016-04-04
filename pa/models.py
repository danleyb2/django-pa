from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User ,related_name='user_profile')
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])