from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
import views

urlpatterns = [
    url(r'^$', login_required(views.HomeView.as_view())),
    url(r'^logout/$', 'homepage.views.logout_view', name='logout'),
    url(r'^home', login_required(views.HomeView.as_view())),
    url(r'^eventDetail', login_required(views.EventDetailView.as_view())),
    url(r'^profile', views.ProfileView.as_view(), name='profile'),
    url(r'^index', views.IndexView.as_view()),
]
