import json, spotipy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets
from rest_framework.views import APIView
from django.conf import settings
from models import Country, City, Airport, Artist, Show
from sabreapi import Sabre
from serializers import CountrySerializer, CitySerializer, AirportSerializer, \
    ArtistSerializer, ShowSerializer

class ApiSample(View):
    def get(self, request):
        return HttpResponse(json.dumps(request.GET), content_type='application/json')


class EventsApi(View):
    def get(self, request):
        social_user = request.user.social_auth.get(provider='spotify')
        spotipy_api = spotipy.Spotify(auth=social_user.access_token)
        
        artists = self.find_artists(spotipy_api);
        events = self.find_events(artists)

        return HttpResponse(self.event_to_json(events), content_type='application/json')

    def find_artists(self, spotipy_api):
        followed = spotipy_api.current_user_followed_artists();
        ids = [artist['id'] for artist in followed['artists']['items']]
        return Artist.objects.filter(spotify_id__in=ids)

    def find_events(self, artists):
        return Show.objects.filter(artists__in=artists)

    def event_to_json(self, events):
        events = [{"name": e.venue} for e in events]
        return json.dumps({'events': events})


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


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
