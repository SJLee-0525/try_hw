from rest_framework import serializers
from .models import Location, Station, Car

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class LocationDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Location
            fields = ('address',)
    
    address = LocationDetailSerializer(read_only=True)

    class Meta:
        model = Station
        fields = '__all__'


class StationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('address', 'is_opening',)

class StationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'