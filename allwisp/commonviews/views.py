from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

import datetime

from django.core.files.storage import FileSystemStorage
from apps.customer.models import Customer
from  apps.expenses.models import Expense
from apps.items.models import DocumentItem
from apps.documents.models import Document



# Default document list, show 25 recent documents
@login_required(login_url='login/')
def index(request):
    documents = Document.objects.order_by('-date')[:25]
    context = {
		'title' : 'Recent Documents',
        'document_list' : documents,
    }
    return render(request, 'index.html', context)




# Show big list of all documents
@login_required(login_url='login/')
def all_documents(request):
    documents = Document.objects.order_by('-date')
    context = {
		'title' : 'All Documents',
        'document_list' : documents,
    }
    return render(request, 'index.html', context)



# Show draft documents
@login_required(login_url='login/')
def draft_documents(request):
    documents = Document.objects.filter(status='Draft').order_by('-date')
    context = {
		'title' : 'Draft Documents',
        'document_list' : documents,
    }
    return render(request, 'index.html', context)



# Show paid documents
@login_required(login_url='login/')
def paid_documents(request):
    documents = Document.objects.filter(status='Paid').order_by('-date')
    context = {
		'title' : 'Paid Documents',
        'document_list' : documents,
    }
    return render(request, 'index.html', context)



# Show unpaid documents
@login_required(login_url='login/')
def unpaid_documents(request):
    documents = Document.objects.filter(status='Unpaid').order_by('-date')
    context = {
		'title' : 'Unpaid Documents',
        'document_list' : documents,
    }
    return render(request, 'index.html', context)



# Display a specific document
@login_required(login_url='login/')
def document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    context = {
		'title' : 'Document ' + str(document_id),
	    'document' : document,
	}
    return render(request, 'document.html', context)



# Search for document
@login_required(login_url='login/')
def search_document(request):
    id = request.POST['id']
    return HttpResponseRedirect(reverse('document', args=(id,)))



# Create new document
@login_required(login_url='login/')
def new_document(request):
	# If no customer_id is defined, create a new document
	if request.method=='POST':
		customer_id = request.POST['customer_id']

		if customer_id=='None':
			customers = Customer.objects.order_by('ragionesociale')
			context = {
				'title' : 'Nuova fattura',
				'customer_list' : customers,
				'error_message' : 'Seleziona un cliente dalla lista',
				}
			return render(request, 'new_document.html', context)
		else:
			customer = get_object_or_404(Customer, pk=customer_id)
			i = Document(customer=customer, date=datetime.date.today(), status='Unpaid')
			i.save()
			return HttpResponseRedirect(reverse('document', args=(i.id,)))

	else:
		# Customer list needed to populate select field
		customers = Customer.objects.order_by('ragionesociale')
		context = {
			'title' : 'Nuova fattura',
			'customer_list' : customers,
		}
		return render(request, 'new_document.html', context)



# Print document
@login_required(login_url='login/')
def print_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    context = {
		'title' : "Document " + str(document_id),
	    'document' : document,
	}
    return render(request, 'print_document.html', context)



# Delete an document
@login_required(login_url='login/')
def delete_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.delete()
    return HttpResponseRedirect(reverse('index'))



# Update document
@login_required(login_url='login/')
def update_document(request, document_id):
	document = get_object_or_404(Document, pk=document_id)
	try:
		document.date = datetime.datetime.strptime(request.POST['date'], "%m/%d/%Y")
		document.status = request.POST['status']
		document.save()
	except (KeyError, Document.DoesNotExist):
		return render(request, 'document.html', {
			'document': document,
			'error_message': 'Si è verificato un problema, non sono stato in grado di aggiornare la fattura',
		})
	else:
		context = {
			'confirm_update' : True,
			'title' : 'Document ' + str(document_id),
			'document' : document,
			}
		return render(request, 'document.html', context)



# Upload attachment for document
@login_required(login_url='login/')
def upload_document_attachment(request, document_id):
    myfile = request.FILES['file']
    document = get_object_or_404(Document, pk=document_id)

    fs = FileSystemStorage()
    fs.save(myfile.name, myfile)

    e = document.documentattachment_set.create(file=myfile, displayname=myfile.name)
    e.save()

    return HttpResponseRedirect(reverse('document', args=(document.id,)))



# Delete attachment from document
@login_required(login_url='login/')
def delete_document_attachment(request, document_id, documentattachment_id):
	document = get_object_or_404(Document, pk=document_id)
	documentattachment = get_object_or_404(DocumentAttachment, pk=documentattachment_id)
	try:
		documentattachment.delete()
		fs = FileSystemStorage()
		fs.delete(documentattachment)
	except:
		context = {
			'error_message' : "Unable to delete attachment!",
			'document_id' : document_id
		}
		return render(request, 'view_document.html', context)
	else:
		return HttpResponseRedirect(reverse('document', args=(document.id,)))

# User login
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if (user is not None):
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			context = {
				'error_message' : 'Non siamo riusciti a identificarti. Per favore controlla username e password',
				}
			return render(request, 'project/login.html', context)
	else:
		return render(request, 'project/login.html')



# User logout
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

# Administrative settings
def users(request):
    return None


def settings(request):
    return None
