from rest_framework import viewsets
from core.models import State
from core.serializers import StateSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

from rest_framework import viewsets
from core.models import Currency
from core.serializers import CurrencySerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
