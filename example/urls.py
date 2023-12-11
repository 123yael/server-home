# example/urls.py
from django.urls import path

from example.views import index
from example.views import name

urlpatterns = [
    path('', index),
    path('name', name)
]