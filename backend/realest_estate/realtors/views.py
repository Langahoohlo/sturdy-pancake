from django.shortcuts import render
from rest_framework import permissions
from .models import Realtor
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import RealtorSerializer
from django.views.decorators.csrf import csrf_exempt


class RealtorsListView(ListAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination = None

class RealtorView(RetrieveAPIView):
    # permissions_classes = (permissions.AllowAny)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer


class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None
