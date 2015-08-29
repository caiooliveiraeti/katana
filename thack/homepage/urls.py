from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required, permission_required
import views

urlpatterns = [
    url(r'^$', views.Home.as_view()),

    url(r'^home', login_required(views.Home.as_view())),
    url(r'^index', views.Index.as_view()),
]
