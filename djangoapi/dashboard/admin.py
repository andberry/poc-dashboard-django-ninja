from django.contrib import admin
from .models import Customer, Invoice, Product, Document

class CustomerAdmin(admin.ModelAdmin):
  list_display = ['name', 'email']

class InvoiceAdmin(admin.ModelAdmin):
  list_display = ['customer', 'amount', 'date']
  list_filter = ['amount', 'date']

class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price']

class DocumentAdmin(admin.ModelAdmin):
  list_display = ['title', 'type', 'uploadDate', 'updateDate']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Document, DocumentAdmin)
