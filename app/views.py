from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Room
from .serializers import RoomSerializer, UserSerializer, SignInSerializer


@api_view()
def rooms_view(request):
    rooms_queryset = Room.objects.all()
    serializer = RoomSerializer(rooms_queryset, many=True)

    return Response(serializer.data)

@api_view()
def room_view(request, room_name):
    chat_room = None
    
    try:
        chat_room = Room.objects.get(name=room_name)

    except:
        chat_room = Room.objects.create(name=room_name)

    serializer = RoomSerializer(chat_room)
    return Response(serializer.data)

class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class SignInView(TokenObtainPairView):
    serializer_class = SignInSerializer