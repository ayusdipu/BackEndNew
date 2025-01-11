from django.shortcuts import render
from rest_framework import viewsets
from Produk.models import Produk, ProdukPromotion
from Produk.serializers import ProdukPromotionSerailizer, ProdukSerailizer
# Create your views here.

class ProdukView(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerailizer

class ProdukPromotionView(viewsets.ModelViewSet):
    queryset = ProdukPromotion.objects.all()
    serializer_class = ProdukPromotionSerailizer
    