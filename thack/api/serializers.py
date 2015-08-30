from rest_framework import serializers
from models import Country, City, Airport, Artist, Show


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
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    class Meta:
        model = Artist
        fields = ('id', 'spotify_id', 'name', 'popularity', 'genres')


class ShowSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)
    artists = ArtistSerializer(many=True, read_only=True)
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return unicode(obj)

    class Meta:
        model = Show
        fields = ('id', 'name', 'description', 'city', 'lat', 'lon', 'datetime', 'artists', 'address', 'price', 'image')
