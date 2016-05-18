from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Technology,Service,Location,Project,SiteInfo,Contact,Icon
# Register your models here.

ua = admin.site._registry[User]
admin_class = ua.__class__


admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 0
    
class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0
    
class LocationInline(admin.TabularInline):
    model = Location
    
class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0

class UserProfileAdmin1(admin_class):
    inlines = tuple(admin_class.inlines)+(UserProfileInline, )
    model  = User


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    
class SiteInfoAdmin(admin.ModelAdmin):
    model = SiteInfo 
    inlines = (TechnologyInline,ServiceInline,ProjectInline)


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(User,UserProfileAdmin1)
admin.site.register([Technology,Service,Project,Location,Contact,Icon])
admin.site.register(SiteInfo,SiteInfoAdmin)
