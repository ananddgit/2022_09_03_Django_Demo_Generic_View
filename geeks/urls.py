from django.urls import path

# importing views from views..py
from .views import GeeksList
urlpatterns = [
    path('demogeeks/', GeeksList.as_view()),
]