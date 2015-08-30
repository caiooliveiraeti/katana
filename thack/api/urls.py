from django.conf.urls import url, include
from django.contrib.auth.models import User
from views import ApiSample, EventsApi, EventFares
from rest_framework import routers
from django.contrib.auth.decorators import login_required, permission_required

router = routers.DefaultRouter()
router.register(r'sample', ApiSample, base_name='sample')

urlpatterns = [
    url(r'sample', login_required(ApiSample.as_view())),
    url(r'events', login_required(EventsApi.as_view())),
    url(r'eventFares', login_required(EventFares.as_view())),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
