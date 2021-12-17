from django.urls import path
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url



urlpatterns = [
    
    # # # INVOICE EXPENSES

    path('<int:invoice_id>/expenses/add/', views.add_invoice_expense, name='add_invoice_expense'),
    path('<int:invoice_id>/expenses/<int:expense_id>/delete/', views.delete_invoice_expense, name='delete_invoice_expense'),
   
]