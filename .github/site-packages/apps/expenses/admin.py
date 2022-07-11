from django.contrib import admin

# Register your models here.

from .models import Expense

admin.site.register(Expense)
