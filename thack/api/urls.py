from django.conf.urls import url, include
from django.contrib.auth.models import User
from views import ApiSample
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sample', ApiSample, base_name='sample')

urlpatterns = [
    url(r'sample/', ApiSample.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
