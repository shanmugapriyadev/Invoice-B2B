from rest_framework import serializers
from .models import Company, CompanyAddress, CompanyGSTNumber, CompanyPaymentMode


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'handle']


class CompanyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAddress
        fields = ['id', 'company', 'name', 'address_line_1', 'address_line_2', 'address_line_3', 'city', 'state']


class CompanyGSTNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyGSTNumber
        fields = ['id', 'company', 'gst_number', 'state', 'deactivated_on']


class CompanyPaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPaymentMode
        fields = ['id', 'company', 'mode', 'value']
