from django.shortcuts import render
from rest_framework import viewsets
from Pembelian.serializers import NotaPembelianSerializer, DetailPembelianSerializer
from Pembelian.models import NotaPembelian, DetailPembelian
# Create your views here.

class NotaPembelianView(viewsets.ModelViewSet):
    queryset = NotaPembelian.objects.all()
    serializer_class = NotaPembelianSerializer

class DetailPembelianView(viewsets.ModelViewSet):
    queryset = DetailPembelian.objects.all()
    serializer_class = DetailPembelianSerializer