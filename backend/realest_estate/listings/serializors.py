from rest_framework import serializers
from .models import Listings

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = ('title', 'address', 'city', 'district', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqm', 'display_photo', 'slug')

class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = '__all__'
        lookup_field = 'slug'