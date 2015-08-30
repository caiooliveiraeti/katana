import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from django.conf import settings


class ApiSample(View):
    def get(self, request):
        return HttpResponse(json.dumps(request.GET), content_type='application/json')

class EventsApi(View):
    def get(self, request):
        return HttpResponse(json.dumps(request.GET), content_type='application/json')


class EventFares(View):
    def get(self, request):
    	sabre = Sabre(settings.SABRE_KEY, settings.SABRE_SECRET)
		fares = sabre.api.v1.historical.flights.fares(
			origin=request.GET['origin'],
			destination=request.GET['origin'],
			earliestdeparturedate=request.GET['earliestdeparturedate'],
			latestdeparturedate=request.GET['latestdeparturedate'],
			lengthofstay=7,
		)
        return HttpResponse(json.dumps(fares), content_type='application/json')
