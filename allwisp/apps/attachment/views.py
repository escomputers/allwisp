from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime

from apps.customer.models import Customer
from apps.attachment.models import InvoiceAttachment,ExpenseAttachment
from  apps.expenses.models import Expense
from apps.items.models import InvoiceItem
from apps.invoices.models import Invoice
from .models import InvoiceAttachment,ExpenseAttachment
# Create your views here.

# Upload attachment for invoice
@login_required(login_url='login/')
def upload_invoice_attachment(request, invoice_id):
    myfile = request.FILES['file']
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    fs = FileSystemStorage()
    fs.save(myfile.name, myfile)

    e = invoice.invoiceattachment_set.create(file=myfile, displayname=myfile.name)
    e.save()

    return HttpResponseRedirect(reverse('invoice', args=(invoice.id,)))



# Delete attachment from invoice
@login_required(login_url='login/')
def delete_invoice_attachment(request, invoice_id, invoiceattachment_id):
	invoice = get_object_or_404(Invoice, pk=invoice_id)
	invoiceattachment = get_object_or_404(InvoiceAttachment, pk=invoiceattachment_id)
	try:
		invoiceattachment.delete()
		fs = FileSystemStorage()
		fs.delete(invoiceattachment)
	except:
		context = {
			'error_message' : "Unable to delete attachment!",
			'invoice_id' : invoice_id
		}
		return render(request, 'view_invoice.html', context)
	else:
		return HttpResponseRedirect(reverse('invoice', args=(invoice.id,)))
