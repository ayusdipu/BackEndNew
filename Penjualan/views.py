from django.shortcuts import render
from rest_framework import viewsets
from Penjualan.models import NotaPenjualan, DetailPenjualan
from Penjualan.serializers import NotaPenjualanSerializer, DetailPenjualanSerializer
# Create your views here.

class NotaPenjualanView(viewsets.ModelViewSet):
    queryset = NotaPenjualan.objects.all()
    serializer_class = NotaPenjualanSerializer

class DetailPenjualanView(viewsets.ModelViewSet):
    queryset = DetailPenjualan.objects.all()
    serializer_class = DetailPenjualanSerializer
    