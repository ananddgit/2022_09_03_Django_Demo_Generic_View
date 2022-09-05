from django.shortcuts import render
from django.views.generic.list import ListView
from demo.models import Publisher
from demo.models import Author

# Create your views here.
class PublisherList(ListView):
    model = Publisher

class AuthorList(ListView):
    model = Author