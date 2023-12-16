from rest_framework.serializers import ModelSerializer
from events.models import DevEvent
class DevEventSerializer(ModelSerializer):
    
    class Meta:

        model = DevEvent
        fields = '__all__'