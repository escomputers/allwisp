from django.http import JsonResponse,HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.core.files.storage import FileSystemStorage
import json, os
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.models import model_to_dict
from ..forms import clientiForm, statoclienteForm,offertainternetForm, cadenzapagamentoform, metodopagamento, offertavoipForm
from .models import Customer
from apps.attachment.models import InvoiceAttachment,ExpenseAttachment
from  apps.expenses.models import Expense
from apps.items.models import InvoiceItem,InvoiceItem, offertainternet, cadenzapagamento, metodopagamento
from apps.invoices.models import Invoice
from django.views.generic.edit import UpdateView

#new customer
@login_required(login_url='login/')
def nuovocliente(request):
	clienti=clientiForm(request.POST)
	if clienti.is_valid():
		clienti.save()
		return render(request, 'nuovocliente.html', context={'clienti': clientiForm()})
	return render(request, 'nuovocliente.html',context={'clienti': clientiForm()})


# Create your views here.
# List all customers
@login_required(login_url='login/')
def customer_list(request):
	customers = Customer.objects.all()
	context = {
		'title' : 'Customer List',
		'customers' : customers,
	}
	return render(request, 'customers.html', context)



# Update customer

def update_customer(request, ragionesociale):
		custom = Customer.objects.get(pk=ragionesociale)
		if request.method == "POST":
			clienti=clientiForm(request.POST, instance=custom)
			if clienti.is_valid():
				custom = clienti.save(commit=False)
				custom.save()
				return render( request, 'customer.html', context={'clienti': clienti})
				#return HttpResponseRedirect(reverse('update', args=(custom.ragionesociale,)))
		else:
			clienti=clientiForm( instance=custom )		
		return render( request, 'customer.html', context={'clienti': clienti})
            


# Delete customer
@login_required(login_url='login/')
def delete_customer(request, ragionesociale):
	customer = get_object_or_404(Customer, pk=ragionesociale)
	customer.delete()
	return HttpResponseRedirect(reverse('customer_list'))


@login_required(login_url='login/')
def statocliente(request):
		formstato=statoclienteForm(request.POST)
		if formstato.is_valid():
			formstato.save()
			return render(request, 'statocliente.html', context={'formstato': statoclienteForm()})
		return render(request, 'statocliente.html', context={'formstato': statoclienteForm()})