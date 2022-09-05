from django.urls import path
from demo.views import PublisherList

urlpatterns = [
    path('publishers/', PublisherList.as_view()),
]