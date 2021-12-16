from __future__ import unicode_literals
import os
import datetime
from django import forms
from django.db import connections
from django.core.files.storage import FileSystemStorage
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from apps.attachment.models import InvoiceAttachment, ExpenseAttachment
from  apps.expenses.models import Expense
from apps.items.models import InvoiceItem, offertainternet, cadenzapagamento, metodopagamento, offertavoip
from apps.invoices.models import Invoice
from internationalflavor.vat_number import VATNumberField
from internationalflavor.iban import IBANField


class statocliente (models.Model):
	stato_del_cliente = models.CharField(max_length=256)
	def __str__(self):
		return self.stato_del_cliente

def get_metodopagamento():
    return metodopagamento.objects.get_or_create(id=1)

# Create your models here.
class Customer (models.Model):
	customer_id=models.IntegerField()
	ragionesociale = models.CharField(max_length=256)
	scelta_fattura = models.BooleanField()
	codicefiscale = models.CharField(max_length=256,blank=True)
	piva = VATNumberField(max_length=256, blank=True)
	codiceunivoco_sdi = models.CharField(max_length=128, blank=True)
	pec = models.EmailField()
	indirizzo_res = models.CharField(max_length=256,blank=True)
	comune_res = models.CharField(max_length=256,blank=True)
	cap_res = models.CharField(max_length=128,blank=True)
	prov_res = models.CharField(max_length=128,blank=True)
	indirizzo_inst = models.CharField(max_length=128, blank=True)
	comune_inst = models.CharField(max_length=128, blank=True)
	cap_inst = models.CharField(max_length=128, blank=True)
	prov_inst = models.CharField(max_length=128, blank=True)
	email = models.EmailField()
	recapito_tel = PhoneNumberField(default='+39')
	fax = PhoneNumberField(blank=True, default='+39')
	coordinate_gps = models.CharField(max_length=512, blank=True)
	offerta_internet = models.ForeignKey(offertainternet, on_delete=models.CASCADE,blank=True, null=True,  related_name="tags") 
	cadenza_pagamento = models.ForeignKey(cadenzapagamento, on_delete=models.CASCADE, blank=True, null=True,  related_name="tags") 
	metodo_pagamento = models.ForeignKey(metodopagamento, on_delete=models.CASCADE, blank=True, null=True,  related_name="tags", default=get_metodopagamento) 
	importo_attivazione = models.IntegerField(blank=True, default=0)
	importo_offerta_dedicata = models.FloatField(blank=True, default=0.0)
	codice_iban = IBANField()
	spese_invio_bolletta = models.FloatField(blank=True, default=0.0)
	offerta_voip =models.ForeignKey(offertavoip, on_delete=models.CASCADE,blank=True,  null=True,  related_name="tags")
	numero_voip =numero_voip =PhoneNumberField( default='Italy +39',blank=True)
	nodo = models.CharField(max_length=128, blank=True)
	ip_statico = models.GenericIPAddressField()
	mac_adress = models.CharField(max_length=128, blank=True)
	note = models.TextField(blank=True)
	stato_cliente=models.ForeignKey(statocliente, on_delete=models.CASCADE,blank=True, null=True,  related_name="tags") 
	data_inizio_contratto=models.DateField(default=datetime.date.today)
	

	def __str__(self):
		return self.ragionesociale
	
	def invoices(self):
		return Invoice.objects.filter(customer=self).count()

