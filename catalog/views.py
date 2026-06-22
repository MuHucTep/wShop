from django.http import HttpResponse
from django.shortcuts import render
from .models import GiftModel, CategoryModel

def root_view(request):
    return render(request, 'index.html', context={'gifts': GiftModel.objects.all(), 'categories': CategoryModel.objects.all()})
