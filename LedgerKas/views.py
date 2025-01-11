from django.shortcuts import render
from LedgerKas.models import Kas, MasterAkun, TabelNeracaAwal, JurnalEntry
from LedgerKas.serializers import KasSerializer, MasterAkunSerializer, TabelNeracaAwalSerializer, JurnalEntrySerializer
from rest_framework import viewsets
# Create your views here.

class KasView(viewsets.ModelViewSet):
    queryset = Kas.objects.all()
    serializer_class = KasSerializer

class MasterAkunView(viewsets.ModelViewSet):
    queryset = MasterAkun.objects.all()
    serializer_class = MasterAkunSerializer

class TabelNeracaAwalView(viewsets.ModelViewSet):
    queryset = TabelNeracaAwal.objects.all()
    serializer_class = TabelNeracaAwalSerializer

class JurnalEntryView(viewsets.ModelViewSet):
    queryset = JurnalEntry.objects.all()
    serializer_class = JurnalEntrySerializer
    