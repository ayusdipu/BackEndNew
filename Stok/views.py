from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from Stok.serializers import StokSerializer, StokTransitSerializer, LokasiStokSerializer
from Stok.models import StokUtama, StokTransit, LokasiStok
# Create your views here.

class StokUtamaFilter(filters.FilterSet):
  
    timestamp = filters.DateFromToRangeFilter()
   
    class Meta:
        model = StokUtama
        fields = ['id','nama_produk','kode_produk','jumlah_barang','gudang_cabang',
                'detail_lokasi','timestamp','harga_beli_weighted','divisi_kantor',
                'perusahaan_kantor'
        ]


class StokView(viewsets.ModelViewSet):
    queryset = StokUtama.objects.all()
    serializer_class = StokSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = StokUtamaFilter

class StokTransitView(viewsets.ModelViewSet):
    queryset = StokTransit.objects.all()
    serializer_class = StokTransitSerializer

class LokasiStokView(viewsets.ModelViewSet):
    queryset = LokasiStok.objects.all()
    serializer_class = LokasiStokSerializer
    
