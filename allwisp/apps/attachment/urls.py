from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
       path('<int:invoice_id>/attachments/add/', views.upload_invoice_attachment, name='upload_invoice_attachment'),
       path('<int:invoice_id>/attachments/<int:invoiceattachment_id>/delete/', views.delete_invoice_attachment, name='delete_invoice_attachment'),
       
]