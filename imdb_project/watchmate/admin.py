from django.contrib import admin
from watchmate.models import Movie, SteamingPlatform, Review

# Register your models here.

admin.site.register(Movie)
admin.site.register(SteamingPlatform)
admin.site.register(Review)