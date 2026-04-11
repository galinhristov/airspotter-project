from django.contrib import admin
from aviation.models import Airline, Airport, Aircraft


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name', 'icao_code', 'iata_code', 'country', 'is_active')
    list_fields = ('name', 'icao_code', 'iata_code')
    list_filter = ('country', 'is_active')


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'iata_code', 'icao_code', 'city', 'country')
    search_fields = ('name', 'iata_code', 'icao_code', 'city')
    list_filter = ('country',)



@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('registration', 'manufacturer', 'model', 'aircraft_type', 'airline', 'is_active')
    search_fields = ('registration', 'manufacturer', 'model')
    list_filter = ('aircraft_type', 'is_active', 'airline')