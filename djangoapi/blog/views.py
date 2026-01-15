from django.shortcuts import render
from django.http import HttpResponse

def blogIndex(request):
  return HttpResponse('blogIndex response')
