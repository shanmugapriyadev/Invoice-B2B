from rest_framework import serializers
from .models import Invoice
from company.serializers import CompanySerializer


class InvoiceSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Invoice
        fields = '__all__'
