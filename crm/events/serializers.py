from rest_framework.serializers import ModelSerializer,StringRelatedField
from events.models import DevEvent,EventType

class DevEventTypeSerializer(ModelSerializer):

    class Meta:
        model = EventType
        fields= '__all__'
class DevEventSerializer(ModelSerializer):
    event_type = DevEventTypeSerializer()
    class Meta:
        model = DevEvent
        fields = '__all__'