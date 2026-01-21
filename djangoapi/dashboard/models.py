from django.db import models
from django.utils.timezone import now

# Create your models here.
class Customer(models.Model):
  def __str__(self):
    return self.name

  name = models.CharField()
  email = models.CharField()

INVOICE_STATUS = {
  "PENDING": 'Pending',
  "PAID": "Paid",
  "CANCELLED": "Cancelled"
}

class Invoice(models.Model):
  def __str__(self):
    return f"{self.customer} ({self.amount} EUR)"

  customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateTimeField()
  status = models.CharField(choices=INVOICE_STATUS)

class Product(models.Model):
  def __str__(self):
    return self.name
  
  name = models.CharField()
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)


DOCUMENT_TYPE = {
  'REPORT': 'Report',
  'LEGAL': 'Legal',
  'FINANCE': 'Finance',
  'MEDIA': 'Media'
}
class Document(models.Model):
  def __str__(self):
    return self.title
  
  title = models.CharField()
  file = models.FileField(upload_to="documents/")
  uploadDate = models.DateTimeField(auto_now_add=True)
  updateDate = models.DateTimeField(default=now )
  type = models.CharField(choices=DOCUMENT_TYPE)