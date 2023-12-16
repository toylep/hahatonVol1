from django.urls import path
from events.views import DevEventListView
urlpatterns = [
    path('',DevEventListView.as_view())
]
