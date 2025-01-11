from django.shortcuts import render
from rest_framework import viewsets
from Salesman.serializers import TugasSalesmanSerializer, TargetSalesmanSerializer
from Salesman.models import TugasSalesman, TargetSalesman
# Create your views here.

class TugasSalesmanView(viewsets.ModelViewSet):
    queryset = TugasSalesman.objects.all()
    serializer_class = TugasSalesmanSerializer

class TargetSalesmanView(viewsets.ModelViewSet):
    queryset = TargetSalesman.objects.all()
    serializer_class = TargetSalesmanSerializer