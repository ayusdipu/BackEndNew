from django.shortcuts import render

from rest_framework import viewsets
from SuratJalanMasuk.models import SJMasuk, DetailSJMasuk
from SuratJalanMasuk.serializers import SJMasukSerializer, DetailSJMasukSerializer

class SJMasukView(viewsets.ModelViewSet):
    queryset = SJMasuk.objects.all()
    serializer_class = SJMasukSerializer

class DetailSJMasukView(viewsets.ModelViewSet):
    queryset = DetailSJMasuk.objects.all()
    serializer_class = DetailSJMasukSerializer
