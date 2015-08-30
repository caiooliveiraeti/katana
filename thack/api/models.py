from django.db import models

from sabreapi import Sabre

sabre = Sabre(
    client_id='V1:8y1tk3qc9kb9s0ta:DEVCENTER:EXT',
    client_secret='hCfAs6B6'
)


class Country(models.Model):
    name = models.CharField(max_length=100)
    destination = models.BooleanField(default=False)
    origin = models.BooleanField(default=False)
    iata = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    iata = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    iata = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class Show(models.Model):
    artist = models.ForeignKey(Artist)
    city = models.ForeignKey(City)
    datetime = models.DateTimeField()
    venue = models.TextField()
    tickets = models.URLField(blank=True, null=True)
