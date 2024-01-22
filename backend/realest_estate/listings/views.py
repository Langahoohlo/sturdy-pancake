from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listings
from .serializors import ListingSerializer, ListingDetailSerializer
from datetime import datetime, timezone, timedelta

class ListingsView(ListAPIView):
    queryset = Listings.objects.order_by('-list_date').filter(is_published=True)
    permission_classes = [permissions.AllowAny]  # Use a list for consistency
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class ListingView(RetrieveAPIView):
    queryset = Listings.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'

class SearchView(ListAPIView):
    permission_classes = [permissions.AllowAny]  # Use a list for consistency
    serializer_class = ListingSerializer

    def post(self, request, format=None):
        queryset = Listings.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        # Mapping for price, bedrooms, bathrooms, sqm, days_passed, has_photos
        price_mapping = {'$0+': 0, '$200,000+': 200000, '$400,000+': 400000, '$600,000+': 600000,
                         '$800,000+': 800000, '$1,000,000+': 1000000, '$1,200,000+': 1200000,
                         '$1,500,000+': 1500000, 'Any': -1}

        bedrooms_mapping = {'0+': 0, '1+': 1, '2+': 2, '3+': 3, '4+': 4, '5+': 5, 'Any': -1}

        bathrooms_mapping = {'0+': 0.0, '1+': 1.0, '2+': 2.0, '3+': 3.0, '4+': 4.0}

        sqm_mapping = {'1000+': 1000, '1200+': 1200, '1500+': 1500, '2000+': 2000, 'Any': 0}

        days_passed_mapping = {'1 or less': 1, '2 or less': 2, '5 or less': 5, '10 or less': 10,
                               '20 or less': 20, 'Any': 0}

        has_photos_mapping = {'1+': 1, '3+': 3, '5+': 5, '10+': 10}

        # Price
        price = price_mapping.get(data['price'], -1)
        if price != -1:
            queryset = queryset.filter(price__gte=price)

        # Bedrooms
        bedrooms = bedrooms_mapping.get(data['bedrooms'], -1)
        queryset = queryset.filter(bedrooms__gte=bedrooms)

        # Home Type
        queryset = queryset.filter(home_type__iexact=data['home_type'])

        # Bathrooms
        bathrooms = bathrooms_mapping.get(data['bathrooms'], -1)
        queryset = queryset.filter(bathrooms__gte=bathrooms)

        # Square Meters
        sqm = sqm_mapping.get(data['sqm'], 0)
        if sqm != 0:
            queryset = queryset.filter(sqm__gte=sqm)

        # Days Listed
        days_passed = days_passed_mapping.get(data['days_listed'], 0)
        if days_passed != 0:
            queryset = [query for query in queryset if
                        (datetime.now(timezone.utc) - query.list_date).days <= days_passed]

        # Has Photos
        has_photos = has_photos_mapping.get(data['has_photos'], 0)
        if has_photos != 0:
            queryset = [query for query in queryset if sum(1 for photo in
                                                           [query.list_photo_1, query.list_photo_2, query.list_photo_3,
                                                            query.list_photo_4, query.list_photo_5, query.list_photo_6,
                                                            query.list_photo_7, query.list_photo_8, query.list_photo_9,
                                                            query.list_photo_10, query.list_photo_12]
                                                           if photo) >= has_photos]

        # Open House
        queryset = queryset.filter(open_house__iexact=data['open_house'])

        # Keywords
        queryset = queryset.filter(description__icontains=data['keywords'])

        serializer = ListingSerializer(queryset, many=True)

        return Response(serializer.data)
