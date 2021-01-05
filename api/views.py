from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
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

    @action(detail=True, methods=['POST'])
    def set_as_owned(self, request, pk=None):
        message = {}
        if pk:
            game = Game.objects.get(pk=pk)
            message = {'game': game.name}
        return Response(message, status=status.HTTP_200_OK)


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
