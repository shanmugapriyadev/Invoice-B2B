# Generated by Django 5.0.1 on 2024-01-25 09:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=255, unique=True)),
                ('invoice_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('line_items', models.JSONField()),
                ('sub_total', models.IntegerField()),
                ('cgst', models.IntegerField(null=True)),
                ('sgst', models.IntegerField(null=True)),
                ('igst', models.IntegerField(null=True)),
                ('exempt_gst', models.BooleanField(default=False)),
                ('total', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]