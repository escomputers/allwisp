from __future__ import unicode_literals
from django.db import models
from django.db import connections
from django.core.files.storage import FileSystemStorage


class InvoiceItem(models.Model):
	invoice = models.ForeignKey('invoices.Invoice', on_delete=models.CASCADE)
	name = models.CharField(max_length=128)
	description = models.TextField()
	cost = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	vat = models.IntegerField()
	ivadec=models.IntegerField(default=100)
	
	def total(self):
		return self.cost * self.qty + (self.iva * self.cost * self.qty / self.ivadec)


class offertainternet(models.Model):
	nomeofferta = models.CharField(max_length=256)
	prezzo = models.FloatField()
	iva = models.IntegerField()
	descrizione = models.TextField()
	totaleivato = models.FloatField()

	def __str__(self):
		return self.nomeofferta

class offertavoip(models.Model):
	nomeofferta = models.CharField(max_length=256)
	prezzo = models.FloatField()
	iva = models.IntegerField()
	descrizione = models.TextField()
	totaleivato = models.FloatField()

	def __str__(self):
		return self.nomeofferta

class cadenzapagamento(models.Model):
	periodi=models.CharField(max_length=128)
	numero_mese=models.IntegerField()

	def __str__(self):
		return self.periodi

class metodopagamento(models.Model):
	metodo=models.CharField(max_length=128)

	def __str__(self):
		return self.metodo