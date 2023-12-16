from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField
    )
from django.contrib.auth.models import User


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
    class Meta:
        model = User
        fields = '__all__'