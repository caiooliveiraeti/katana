from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout


class IndexView(TemplateView):
    template_name = 'index.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'

class EventDetailView(TemplateView):

    template_name = 'event_detail.html'

    def get_context_data(self, **kwargs):
        d = super(EventDetailView, self).get_context_data(**kwargs)
        d['event_id'] = self.request.GET['event_id']
        return d

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')