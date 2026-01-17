from ninja import NinjaAPI, Schema
from typing import List
from dashboard.models import Customer, Invoice, Product
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
    'jan': 12.31,
    'feb': 22.32,
    'mar': 32.33,
    'apr': 42.34,
    'may': 52.35,
    'jun': 62.36,
    'jul': 72.37,
    'aug': 82.38,
    'sep': 92.39,
    'oct': 102.41,
    'nov': 112.42,
    'dec': 122.43,
  }