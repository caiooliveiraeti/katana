from rest_framework import serializers
from models import Country, City, Airport, Artist


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'iata', 'name', 'cities')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'iata', 'name', 'country')


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('id', 'iata', 'name', 'city')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'spotify_id', 'name')
