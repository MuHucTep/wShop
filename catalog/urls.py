from django.urls import path

from catalog.views import *

urlpatterns = [
    path('', rood_view, name='rood_view'),
]