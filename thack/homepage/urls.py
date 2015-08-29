from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
import views

urlpatterns = [
    url(r'^$', views.Home.as_view()),
    url(r'^logout/$', 'homepage.views.logout_view', name='logout'),
    url(r'^accounts/profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^home', login_required(views.Home.as_view())),
    url(r'^index', views.Index.as_view()),
]
