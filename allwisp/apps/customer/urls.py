from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


    # # # CUSTOMERS
urlpatterns = [
    path('listaclienti/', views.customer_list, name='customer_list'),
    #path('<int:ragionesociale>/', views.customer, name='customer'),
	path('<int:ragionesociale>/', views.update_customer, name='update'),
   # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:ragionesociale>/delete/', views.delete_customer, name='delete_customer'),
    path('newc', views.nuovocliente, name='add_client'),
    path('statocliente', views.statocliente, name='aggiungi_stato'),
]