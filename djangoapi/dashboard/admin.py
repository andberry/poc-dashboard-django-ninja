from django.contrib import admin
from .models import Customer, Invoice, Product

class CustomerAdmin(admin.ModelAdmin):
  list_display = ['name', 'email']

class InvoiceAdmin(admin.ModelAdmin):
  list_display = ['customer', 'amount', 'date']
  list_filter = ['amount', 'date']

class ProductAdmin(admin.ModelAdmin):
  list_display = ['name', 'price']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product, ProductAdmin)
