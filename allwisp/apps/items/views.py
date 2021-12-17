from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from apps.customer.models import Customer
from apps.attachment.models import InvoiceAttachment,ExpenseAttachment
from  apps.expenses.models import Expense
from .models import InvoiceItem, offertainternet, cadenzapagamento, metodopagamento
from apps.invoices.models import Invoice
from ..forms import offertainternetForm, cadenzapagamentoform, metodopagamento, offertavoipForm


# Add invoiceitem to invoice
@login_required(login_url='login/')
def add_item(request, invoice_id):
	invoice = get_object_or_404(Invoice, pk=invoice_id)
	try:
		i = invoice.invoiceitem_set.create(name=request.POST['name'], description=request.POST['description'], cost=request.POST['cost'], qty=request.POST['qty'], vat=request.POST['vat'])
		i.save()
	except (KeyError, Invoice.DoesNotExist):
		return render(request, 'view_invoice.html', {
			'invoice': invoice,
			'error_message': 'Not all fields were completed.',
		})
	else:
		return HttpResponseRedirect(reverse('invoice', args=(invoice.id,)))



# Delete invoiceitem from invoice
@login_required(login_url='login/')
def delete_item(request, invoiceitem_id, invoice_id):

	item = get_object_or_404(InvoiceItem, pk=invoiceitem_id)
	invoice = get_object_or_404(Invoice, pk=invoice_id)
	try:
		item.delete()
	except (KeyError, InvoiceItem.DoesNotExist):
		return render(request, 'view_invoice.html', {
			'invoice': invoice,
			'error_message': 'Item does not exist.',
		})
	else:
		return HttpResponseRedirect(reverse('invoice', args=(invoice.id,)))



# List all prodotto
@login_required(login_url='login/')
def prodotto_list(request):
	prodotti = offerta.objects.all()
	context = {
		'title' : 'Lista prodotti',
		'prodotti' : prodotti,
	}
	return render(request, 'listaprodotti.html', context)



# Add nuova offerta
@login_required(login_url='login/')
def nuova_offerta(request):
		form=offertainternetForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'offertainternet.html', context={'form': offertainternetForm()})
		return render(request, 'offertainternet.html', context={'form': offertainternetForm()})

#prodotto specifico
@login_required(login_url='login/')
def prodotto(request, id):
	prodottospecifico = get_object_or_404(offerta, pk=id)
	context = {
		'title' : "Informazioni sul prodotto - %s" % prodottospecifico.nomeofferta,
		'prodottospecifico' : prodottospecifico,
		
	}
	return render(request, 'prodottospecifico.html', context)

# Update prodotto
@login_required(login_url='login/')
def update_prodotto(request, id):
	# Stuff from form
	d = get_object_or_404(offerta, pk=nomeofferta)
	d.nomeofferta=request.POST['nomeofferta'] 
	d.prezzo=request.POST['prezzo'] 
	d.iva=request.POST['iva'] 
	d.totaleivato=request.POST['totaleivato']

	d.save()

	return HttpResponseRedirect(reverse('prodotto_list', args=(d.id,)))



# Delete prodotto
@login_required(login_url='login/')
def delete_prodotto(request, nomeofferta):
	prodotto= get_object_or_404(offerta, pk=offerta.id)
	prodotto.delete()
	return HttpResponseRedirect(reverse('prodotto_list',))

@login_required(login_url='login/')
def nuovo_periodo(request):
		form=cadenzapagamentoform(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'cadenzapagamento.html', context={'form': cadenzapagamentoform()})
		return render(request, 'cadenzapagamento.html', context={'form': cadenzapagamentoform()})



@login_required(login_url='login/')
def metodo_pagamento(request):
		form=metodopagamento(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'metodopagamento.html', context={'form': metodopagamento()})
		return render(request, 'metodopagamento.html', context={'form': metodopagamento()})

# Add nuova offerta
@login_required(login_url='login/')
def nuova_offerta_voip(request):
		formvoip=offertavoipForm(request.POST)
		if formvoip.is_valid():
			formvoip.save()
			return render(request, 'offertavoip.html', context={'formvoip': offertavoipForm()})
		return render(request, 'offertavoip.html', context={'formvoip': offertavoipForm()})