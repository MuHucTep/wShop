from django.http import HttpResponse
from django.shortcuts import render

def rood_view(request):
    return HttpResponse("Hello, World!")
