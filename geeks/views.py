from django.views.generic.list import ListView
from django.shortcuts import render
from .models import GeeksModel

# Create your views here.
class GeeksList(ListView):
    model = GeeksModel
    