from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Game, Session, Player, PlayerSessionLink, GameOwnership
from api.serializers import (
    GameSerializer,
    SessionSerializer,
    PlayerSerializer,
    GameOwnershipSerializer,
    PlayerSessionLinkSerializer, PlayerMiniSerializer
)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerMiniSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PlayerSerializer(instance)
        return Response(serializer.data)


class GameOwnershipViewSet(viewsets.ModelViewSet):
    queryset = GameOwnership.objects.all()
    serializer_class = GameOwnershipSerializer


class PlayerSessionLinkViewSet(viewsets.ModelViewSet):
    queryset = PlayerSessionLink.objects.all()
    serializer_class = PlayerSessionLinkSerializer
