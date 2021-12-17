from __future__ import unicode_literals
from django.db import connections
from django.core.files.storage import FileSystemStorage
from django.db import models


from  apps.expenses.models import Expense
from apps.invoices.models import Invoice

class InvoiceAttachment(models.Model):
	file = models.FileField(upload_to='invoice/')
	displayname = models.CharField(max_length=128)
	invoice = models.ForeignKey('invoices.Invoice', on_delete=models.CASCADE)

class ExpenseAttachment(models.Model):
	file = models.FileField(upload_to='expense/')
	displayname = models.CharField(max_length=128)
	expense = models.ForeignKey('expenses.Expense', on_delete=models.CASCADE)
