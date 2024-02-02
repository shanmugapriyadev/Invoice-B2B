from django.urls import path, include
from rest_framework.routers import DefaultRouter
from company.views import (
    CompanyViewSet,
    CompanyAddressViewSet,
    CompanyGSTNumberViewSet,
    CompanyPaymentModeViewSet,
)

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'company-addresses', CompanyAddressViewSet, basename='company-address')
router.register(r'company-gst-numbers', CompanyGSTNumberViewSet, basename='company-gst-number')
router.register(r'company-payment-modes', CompanyPaymentModeViewSet, basename='company-payment-mode')

urlpatterns = [path('', include(router.urls)),]
