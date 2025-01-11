from django.shortcuts import render
from Driver.models import Driver
from Driver.serializers import DriverSerializer
from rest_framework import viewsets
# Create your views here.

class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer