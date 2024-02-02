# invoice/models.py
from django.db import models
from company.models import Company
from client.models import Client
from django.contrib.auth.models import User

class Invoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=255, unique=True)
    invoice_date = models.DateTimeField()
    due_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    line_items = models.JSONField()
    sub_total = models.IntegerField()
    cgst = models.IntegerField(null=True)
    sgst = models.IntegerField(null=True)
    igst = models.IntegerField(null=True)
    exempt_gst = models.BooleanField(default=False)
    total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'b2bi_invoices'

    def __str__(self):
        return f"{self.invoice_number} - {self.client}"
