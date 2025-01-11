from django.shortcuts import render

from rest_framework import viewsets
from SuratJalanKeluar.models import SJKeluar, DetailSJKeluar, DetailLokasiKeluarProduk
from SuratJalanKeluar.serializers import SJKeluarSerializer, DetailSJKeluarSerializer, DetailLokasiKeluarProdukSerializer


class SJKeluarView(viewsets.ModelViewSet):
    queryset = SJKeluar.objects.all()
    serializer_class = SJKeluarSerializer

class DetailSJKeluarView(viewsets.ModelViewSet):
    queryset = DetailSJKeluar.objects.all()
    serializer_class = DetailSJKeluarSerializer

class DetailLokasiKeluarProdukView(viewsets.ModelViewSet):
    queryset = DetailLokasiKeluarProduk.objects.all()
    serializer_class = DetailLokasiKeluarProdukSerializer
