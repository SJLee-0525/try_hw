from rest_framework import serializers
from .models import Location, Station, Car


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):

    class LocationAddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = Location
            fields = ('address',)
    
    address = LocationAddressSerializer(read_only=True)

    class Meta:
        model = Station
        fields = '__all__'

class StationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('address', 'is_opening',)
        

        