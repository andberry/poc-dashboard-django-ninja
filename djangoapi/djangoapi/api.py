from ninja import NinjaAPI, Schema
from typing import List
from dashboard.models import Customer, Invoice, Product, Document, DOCUMENT_TYPE
api = NinjaAPI()

# Add
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

# Simple Hello
@api.get("/hello")
def hello(request, name: str = ''):
  if name == '':
    return {"response": "No name provided to say hello"}
  else:
    return {"response": f"Hello {name}"}

# Hello using path for params
@api.get("/hello-from-path/{name}")
def helloFromPath(request, name):
  return {"response": f"Hello {name}"}

# Hello reading params from body
class HelloBodySchema(Schema):
  name: str = 'Berry'

@api.post("/hello-from-body")
def helloFromBody(request, data: HelloBodySchema):
  return f"Responding from helloFromBody: Hey {data.name}!"

# Blog index api
@api.get("/blog")
def blogList(request):
    return {"data": "Blog post list here"}


# Current user info
class UserInfoSchema(Schema):
  username: str
  is_authenticated: bool
  # Unauthenticated users don't have the following fields, so provide defaults.
  email: str = None
  first_name: str = None
  last_name: str = None

@api.get("/user/info", response=UserInfoSchema)
def userInfo(request):
  return request.user

# Dashboard API
# Customers list
class CustomerSchemaOut(Schema):
    name: str
    email: str

@api.get('/customers', response=List[CustomerSchemaOut])
def customersList(request):
  customersQs = Customer.objects.all()
  return customersQs


# Dashboard API
# Invoices list
class InvoiceSchemaOut(Schema):
  customer: CustomerSchemaOut
  amount: float
  status: str

@api.get('/invoices', response=List[InvoiceSchemaOut])
def invoicesList(request):
  invoicesQs = Invoice.objects.all()
  return invoicesQs


# Dashboard API
# Products list
class ProductSchemaOut(Schema):
  name: str
  price: float
  description: str

@api.get('/products', response=List[ProductSchemaOut])
def productsList(request):
  productsQs = Product.objects.all()
  return productsQs


# Dashboard API
# Revenue Data
class RevenueDataSchemaOut(Schema):
  jan: float
  feb: float
  mar: float
  apr: float
  may: float
  jun: float
  jul: float
  aug: float
  sep: float
  oct: float
  nov: float
  dec: float

@api.get('/revenue-data', response=RevenueDataSchemaOut)
def revenueData(request):
  return {
    'jan': 120.31,
    'feb': 220.32,
    'mar': 559.33,
    'apr': 420.34,
    'may': 520.35,
    'jun': 620.36,
    'jul': 349.37,
    'aug': 820.38,
    'sep': 920.39,
    'oct': 458.41,
    'nov': 987.42,
    'dec': 786.43,
  }

@api.get('/latest-invoice', response=InvoiceSchemaOut)
def lastInvoice(request):
  lastInvoicesQs = Invoice.objects.latest('date')
  return lastInvoicesQs

class TotalsSchemaOut(Schema):
  productsTotal: int
  customersTotal: int
  invoicesTotal: int
  documentsTotal: int

@api.get('/totals', response=TotalsSchemaOut)
def totals(request):
  productsCount = Product.objects.count()
  customersCount = Customer.objects.count()
  invoicesCount = Invoice.objects.count()
  documentsCount = Document.objects.count()
  return {
    "productsTotal": productsCount * 10 +1,
    "customersTotal": customersCount * 200 + 24,
    "invoicesTotal": invoicesCount + 300 + 3,
    "documentsTotal": documentsCount + 100 + 1
  }

class DocumentSchemaOut(Schema):
  id: int
  title: str
  file: str
  updateDate: str
  updateDateShort: str
  type: str

  @staticmethod
  def resolve_type(obj):
    return DOCUMENT_TYPE[obj.type]

  @staticmethod
  def resolve_updateDate(obj):
    day = obj.updateDate.day
    return obj.updateDate.strftime(f"%A, {day} %B %Y")
  
  @staticmethod
  def resolve_updateDateShort(obj):
    day = obj.updateDate.day
    return obj.updateDate.strftime(f"{day} %b %Y")

@api.get('/documents', response=List[DocumentSchemaOut])
def documents(request, s: str = ''):
  if s:
    documentsQs = Document.objects.filter(title__contains=s)
  else:
    documentsQs = Document.objects.all()
  return documentsQs

@api.get('/latest-documents', response=List[DocumentSchemaOut])
def lastDocuments(request):
  lastDocumentQs = Document.objects.order_by('updateDate')[0:2]
  return lastDocumentQs