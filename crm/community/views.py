from django.shortcuts import render
from rest_framework.generics import CreateAPIView,GenericAPIView
from django.contrib.auth.models import User
from community.models import MySession
from community.serializers import (
    UserCreateSerializer,
    TgTokenSerializer,
    UserTgTokenSerializer,
    UserFullSerializer)
from rest_framework.response import Response
import uuid

from events.models import DevEvent


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class SessionCreateView(CreateAPIView):
    serializer_class = UserTgTokenSerializer
    
    def post(self,request):

        username = request.data['username']
        token = request.data['token']
        user = User.objects.get(username=username)
        session_id = str(uuid.uuid4())
        if user:
            MySession.create_session(
                user=user,
                session_id=session_id,
                token=token,
            )
        
        return Response("Сессия создана")


class SessionGetView(CreateAPIView):
    serializer_class = TgTokenSerializer
    
    def post(self,request):
        
        s=MySession.objects.get(tg_token = request.data['token']).session_id
        
        return Response({
            'session':s
        })
    
class GetUserView(GenericAPIView):
    
    def get(self,request):
        session_id = request.query_params['session_id']
        session = MySession.objects.get(session_id=session_id)
        user = User.objects.get(id=session.user_id)
        serializer = UserFullSerializer(user)
        result = dict(serializer.data)
        return Response(
            result
        )        


class MatchUserView(GenericAPIView):

    def get(self,request):
        session_id = request.query_params['session_id']
        session = MySession.objects.get(session_id=session_id)
        user = User.objects.get(id=session.user_id)
        match_list=[]
        match_set =[]
        for event in user.devevents.all():
            match_list.extend(event.users.all())
        user_set = set(match_list)
        for u in user_set:
            serializer = UserFullSerializer(u)
            if u != user:
                match_set.append({
                    'user':serializer.data,
                    'rating':(len(list(filter(list(user.specs.all()).__contains__,list(u.specs.all())))))
                })
        
        return Response(match_set)


