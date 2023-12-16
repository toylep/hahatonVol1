from django.shortcuts import render
from rest_framework.generics import ListAPIView
from events.models import DevEvent,EventType
from events.serializers import DevEventSerializer
from community.auth import SessionPermition
# Create your views here.
class DevEventListView(ListAPIView):
    permission_classes = [SessionPermition]
    queryset = DevEvent.objects.select_related(
        'event_type'
        ).all()
    serializer_class = DevEventSerializer