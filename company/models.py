from django.db import models
from core.models import State

class Company(models.Model):
    name = models.CharField(max_length=255)
    handle = models.CharField(max_length=3, unique=True)

    class Meta:
        db_table = 'b2bi_companies'

    def __str__(self):
        return self.name

class CompanyAddress(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    address_line_3 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'b2bi_company_addresses'

    def __str__(self):
        return f"{self.name}, {self.city}, {self.state}"

class CompanyGSTNumber(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    gst_number = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    deactivated_on = models.DateTimeField(null=True)

    class Meta:
        db_table = 'b2bi_company_gst_numbers'

    def __str__(self):
        return f"{self.company} - {self.gst_number}"

class CompanyPaymentMode(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mode = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        db_table = 'b2bi_company_payment_modes'

    def __str__(self):
        return f"{self.company} - {self.mode}"
