from __future__ import unicode_literals
from django.db import models
from django.db import connections
from django.core.files.storage import FileSystemStorage
from django.db import models



# Create your models here.

class Invoice(models.Model):
	customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
	date = models.DateField()
	status = models.CharField(max_length=10)

	def __str__(self):
	    return str(self.id)

	def total_items(self):
		total = 0
		items = self.invoiceitem_set.all()

		for item in items:
			total += item.cost * item.qty

		return total

	def total_expenses(self):
		total = 0
		expenses = self.expense_set.all()

		for expense in expenses:
			total += expense.cost * expense.qty

		return total

	def total(self):
		items = self.total_items()
		expenses = self.total_expenses()

		return items - expenses
		
	def paid(self):
		return self.status == 'Pagato'
		
	def unpaid(self):
		return self.status == 'Non Pagato'
		
	def draft(self):
		return self.status == 'Preventivo'