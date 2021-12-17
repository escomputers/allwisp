from django.contrib import admin

# Register your models here.

from .models import Invoice
from apps.attachment.models import InvoiceAttachment


admin.site.register(Invoice)
