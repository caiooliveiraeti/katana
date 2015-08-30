from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    destination = models.BooleanField(default=False)
    origin = models.BooleanField(default=False)
    iata = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = u'Countries'


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    iata = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name_plural = u'Cities'


class Airport(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)
    iata = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    related = models.ManyToManyField('self')

    def __unicode__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=60)
    genres = models.ManyToManyField(Genre)
    popularity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Show(models.Model):
    artist = models.ManyToManyField(Artist)
    city = models.ForeignKey(City)
    datetime = models.DateTimeField()
    venue = models.TextField()
    tickets = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u"{} at {} in {}".format(self.artist, self.city, self.datetime.strftime('%B'))
