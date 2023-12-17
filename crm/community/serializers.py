from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    StringRelatedField
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
    specs = StringRelatedField(many=True)
    class Meta:
        model = User
        fields = [
            'id',
            'devevents',
            'specs',
            'username',
            'first_name',
            'last_name',
            'is_staff',
        ]