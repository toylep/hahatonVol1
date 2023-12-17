from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField
    )
from django.contrib.auth.models import User
from events.serializers import DevEventSerializer
class UserTgTokenSerializer(Serializer):
    token =  CharField()
    user =  CharField()


class TgTokenSerializer(Serializer):
    token =  CharField()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'is_staff',
        ]


class UserFullSerializer(ModelSerializer):
    devevents = DevEventSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'