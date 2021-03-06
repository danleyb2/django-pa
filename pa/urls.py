__author__ = 'danleyb2 <ndieksman@gmail.com>'

from pa import views
from django.conf.urls import url,include
from rest_framework import routers
from datetime import datetime

urlpatterns = [
    url(r'^index/',views.index),
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'site_data', views.SiteDataViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'send_message', views.MessageSendViewSet)
router.register(r'messages', views.MessagesViewSet)
router.register(r'location', views.LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

from rest_framework.authtoken import views

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]