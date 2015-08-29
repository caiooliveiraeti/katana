from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout


class Home(TemplateView):
    template_name = 'home.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/spotify/')

        return super(ProfileView, self).get(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')