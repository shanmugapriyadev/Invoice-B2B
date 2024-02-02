from rest_framework import viewsets
from company.models import Company
from company.serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


from rest_framework import viewsets
from company.models import CompanyAddress
from company.serializers import CompanyAddressSerializer

class CompanyAddressViewSet(viewsets.ModelViewSet):
    queryset = CompanyAddress.objects.all()
    serializer_class = CompanyAddressSerializer


from rest_framework import viewsets
from company.models import CompanyGSTNumber
from company.serializers import CompanyGSTNumberSerializer

class CompanyGSTNumberViewSet(viewsets.ModelViewSet):
    queryset = CompanyGSTNumber.objects.all()
    serializer_class = CompanyGSTNumberSerializer

from rest_framework import viewsets
from company.models import CompanyPaymentMode
from company.serializers import CompanyPaymentModeSerializer

class CompanyPaymentModeViewSet(viewsets.ModelViewSet):
    queryset = CompanyPaymentMode.objects.all()
    serializer_class = CompanyPaymentModeSerializer

