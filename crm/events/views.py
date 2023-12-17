from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from events.models import DevEvent,EventType
from events.serializers import DevEventSerializer,DevEventTypeSerializer
from community.auth import SessionPermition
# Create your views here.

class DevEventListView(ListCreateAPIView):
    permission_classes = [SessionPermition]
    queryset = DevEvent.objects.select_related(
        'event_type'
        ).all()
    serializer_class = DevEventSerializer


class DevEventTypeCreateView(ListCreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = DevEventTypeSerializer