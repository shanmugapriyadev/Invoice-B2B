# invoice/admin.py
from django.contrib import admin
from .models import Invoice

admin.site.register(Invoice)
