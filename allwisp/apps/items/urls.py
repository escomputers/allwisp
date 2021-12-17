from django.urls import path
from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns =[
	# # # DEFAULT
	path('<int:invoice_id>/item/add/', views.add_item, name='add_item'),
    path('<int:invoice_id>/item/<int:invoiceitem_id>/delete/', views.delete_item, name='delete_item'),
    path('offerta/add/', views.nuova_offerta, name='aggiungi_offerta'),
    path('offerta/add-voip/', views.nuova_offerta_voip, name='aggiungi_offerta_voip'),
    path('offerta/add-periodo/', views.nuovo_periodo, name='aggiungi_periodo'),
    path('offerta/add-metodo-pagamento/', views.metodo_pagamento, name='metodo_pagamento'),
    path('listaprodotti/', views.prodotto_list, name='prodotto_list'),
    path('<int:prodotto>/', views.prodotto, name='prodotto'),
    path('<int:prodotto>/delete/', views.delete_prodotto, name='delete_prodotto'),
    path('<int:prodotto>/update/', views.update_prodotto, name='update_prodotto'),
]

