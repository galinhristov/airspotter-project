from rest_framework import serializers
from sightings.models import Sighting


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = '__all__'
