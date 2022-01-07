from __future__ import unicode_literals
from django.db import connections
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.files.storage import FileSystemStorage



class Expense(models.Model):
	description = models.TextField()
	cost = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	invoice = models.ForeignKey('invoices.Invoice', on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
		
	def total(self):
		return self.cost * self.qty

	def is_business_expense(self):
		return self.invoice is None
