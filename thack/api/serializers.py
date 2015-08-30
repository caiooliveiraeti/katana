from rest_framework import serializers
from models import Country, City


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'pk', 'iata', 'name')

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
