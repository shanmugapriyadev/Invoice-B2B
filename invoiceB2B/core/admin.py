# core/admin.py
from django.contrib import admin
from .models import State, Currency

admin.site.register(State)
admin.site.register(Currency)
