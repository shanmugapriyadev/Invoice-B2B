# core/models.py
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'b2bi_states'

    def __str__(self):
        return self.name

class Currency(models.Model):
    currency_code = models.CharField(max_length=3, unique=True)
    currency = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=10, null=True)
    class Meta:
        db_table = 'b2bi_currencies'

    def __str__(self):
        return self.currency_code
