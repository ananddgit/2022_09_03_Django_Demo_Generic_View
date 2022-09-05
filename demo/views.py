from django.shortcuts import render
from django.views.generic.list import ListView
from demo.models import Publisher

# Create your views here.
class PublisherList(ListView):
    model = Publisher

