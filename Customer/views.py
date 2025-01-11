from django.shortcuts import render
from Customer.serializers import RegisteredCustomerSerializer, LoyaltyPointCustomerSerializer, DataPotensiCustomerSerializer, DailyRegisteredCustomerReportSerializer, KontrakOutletPromotionSerializer
from rest_framework import viewsets
from Customer.models import RegisteredCustomer, LoyaltyPointCustomer, DataPotensiCustomer, DailyRegisteredCustomerReport, KontrakOutletPromotion
# Create your views here.

class RegisteredCustomerView(viewsets.ModelViewSet):
    queryset = RegisteredCustomer.objects.all()
    serializer_class = RegisteredCustomerSerializer

class LoyaltyPointCustomerView(viewsets.ModelViewSet):
    queryset = LoyaltyPointCustomer.objects.all()
    serializer_class = LoyaltyPointCustomerSerializer

class DataPotensiCustomerView(viewsets.ModelViewSet):
    queryset = DataPotensiCustomer.objects.all()
    serializer_class = DataPotensiCustomerSerializer

class DailyRegisteredCustomerReportView(viewsets.ModelViewSet):
    queryset = DailyRegisteredCustomerReport.objects.all()
    serializer_class = DailyRegisteredCustomerReportSerializer

class KontrakOutletPromotionView(viewsets.ModelViewSet):
    queryset = KontrakOutletPromotion.objects.all()
    serializer_class = KontrakOutletPromotionSerializer