from django.contrib import admin
from .models import Customer, Invoice

class CustomerAdmin(admin.ModelAdmin):
  list_display = ['name', 'email']

class InvoiceAdmin(admin.ModelAdmin):
  list_display = ['customer', 'amount', 'date']
  list_filter = ['amount', 'date']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
