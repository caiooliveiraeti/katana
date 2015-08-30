from django.contrib import admin
from models import Country, City, Airport, Artist, Show, Genre

admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Artist)
admin.site.register(Show)
