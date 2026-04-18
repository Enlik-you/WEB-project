from django.contrib import admin
from .models import Region, Country, UserPreference, FavoriteCountry

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(UserPreference)
admin.site.register(FavoriteCountry)