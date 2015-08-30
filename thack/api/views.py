import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework.views import APIView
from django.conf import settings
from models import Country, City, Airport
from sabreapi import Sabre
from serializers import CountrySerializer, CitySerializer, AirportSerializer


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
            destination=request.GET['destination'],
            earliestdeparturedate=request.GET['earliestdeparturedate'],
            latestdeparturedate=request.GET['latestdeparturedate'],
            lengthofstay=request.GET['lengthofstay']
        )
        return HttpResponse(json.dumps(fares), content_type='application/json')


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class AirportViewSet(viewsets.ModelViewSet):
	queryset = Airport.objects.all()
	serializer_class = AirportSerializer
