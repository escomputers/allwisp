from django.contrib import admin

# Register your models here.

from apps.attachment.models import ExpenseAttachment
from .models import Expense

admin.site.register(Expense)