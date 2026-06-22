from django.urls import path

from catalog.views import *

urlpatterns = [
    path('', root_view, name='root_view'),
]