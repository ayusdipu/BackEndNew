from django.shortcuts import render
from rest_framework import viewsets
from Stok.serializers import StokSerializer, StokTransitSerializer, LokasiStokSerializer
from Stok.models import Stok, StokTransit, LokasiStok
# Create your views here.

class StokView(viewsets.ModelViewSet):
    queryset = Stok.objects.all()
    serializer_class = StokSerializer

class StokTransitView(viewsets.ModelViewSet):
    queryset = StokTransit.objects.all()
    serializer_class = StokTransitSerializer

class LokasiStokView(viewsets.ModelViewSet):
    queryset = LokasiStok.objects.all()
    serializer_class = LokasiStokSerializer
    
