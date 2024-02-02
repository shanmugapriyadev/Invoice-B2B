from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import StateViewSet, CurrencyViewSet

router = DefaultRouter()
router.register(r'states', StateViewSet, basename='state')
router.register(r'currencies', CurrencyViewSet, basename='currency')

urlpatterns = [path('', include(router.urls)),]


