from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from itertools import chain
import datetime


from apps.customer.models import Customer
from apps.documents.models import Document
from apps.items.models import DocumentItem
from apps.attachment.models import DocumentAttachment, ExpenseAttachment
from apps.expenses.models import Expense


# Accounting report
@login_required(login_url='login/')
def accounting(request):
	if request.method == 'POST':
		start = datetime.datetime.strptime(request.POST['start'], "%m/%d/%Y")
		end = datetime.datetime.strptime(request.POST['end'], "%m/%d/%Y")
		
		if start > end:
			context = {
				'error_message' : "Start date must be before end date!",
			}
			return render(request, 'accounting.html', context)
		else:
			paiddocuments = Document.objects.filter(date__gt=start).filter(date__lt=end).filter(status = 'Paid')
			alldocuments = Document.objects.filter(date__gt=start).filter(date__lt=end)
			expenses = Expense.objects.filter(date__gt=start).filter(date__lt=end)
			
			# Sum of all paid documents
			documenttotal = 0
			for i in paiddocuments:
				documenttotal += i.total_items()
				
			# Add document expenses within date range, regardless of document status
			for i in alldocuments:
				expenses = list(chain(expenses, Expense.objects.filter(document=i)))
			
			# Sum of all expenses
			expensetotal = 0
			for expense in expenses:
				expensetotal += expense.total()
			
			context = {
				'start' : start,
				'end' : end,
				'documents' : paiddocuments,
				'expenses' : expenses,
				'documenttotal' : documenttotal,
				'expensetotal' : expensetotal,
				'nettotal' : documenttotal - expensetotal,
			}
			return render(request, 'accounting.html', context)
	else:
		return render(request, 'accounting.html')