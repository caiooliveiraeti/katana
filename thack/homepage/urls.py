from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.Home.as_view()),
    url(r'^logout/$', views.logout, name='logout'),
]
