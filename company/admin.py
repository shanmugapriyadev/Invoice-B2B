# company/admin.py
from django.contrib import admin
from .models import Company, CompanyAddress, CompanyGSTNumber, CompanyPaymentMode

admin.site.register(Company)
admin.site.register(CompanyAddress)
admin.site.register(CompanyGSTNumber)
admin.site.register(CompanyPaymentMode)
