from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

class Home(TemplateView):
    template_name = 'home.html'