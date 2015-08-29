from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.Home.as_view()),
    url(r'^logout/$', 'homepage.views.logout_view', name='logout'),
    url(r'^accounts/profile/$', views.ProfileView.as_view(), name='profile'),
]
