import datetime

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from api.models import Game, Session, PlayerSessionLink, GameOwnership
from api.serializers import (
    GameSerializer,
    SessionSerializer,
    UserSerializer,
    UserMiniSerializer,
    GameOwnershipSerializer,
    PlayerSessionLinkSerializer,
)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny, )

    @action(detail=True, methods=['POST'])
    def set_ownership_and_rating(self, request, pk=None):
        if pk:
            game = Game.objects.get(id=pk)
            user = request.user  # type: User
            rating = request.data['rating'] if 'rating' in request.data else None

            try:
                message = self.update_rating(game, rating, user)
                return Response(message, status=status.HTTP_202_ACCEPTED)

            except GameOwnership.DoesNotExist:
                game_ownership = GameOwnership()
                game_ownership.user = user
                game_ownership.rating = rating
                game_ownership.game = game
                game_ownership.save()

                serializer = GameOwnershipSerializer(game_ownership, many=False)
                message = {'message': f"{user.username} successfully registered {game.name}", 'result': serializer.data}
                return Response(message, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    def rate_game(self, request, pk=None):
        if pk:
            game = Game.objects.get(id=pk)
            user = request.user  # type: User
            rating = request.data['rating'] if 'rating' in request.data else None
            try:
                message = self.update_rating(game, rating, user)
                return Response(message, status=status.HTTP_202_ACCEPTED)

            except GameOwnership.DoesNotExist:
                message = {'message': "Rating unowned games is not allowed"}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update_rating(game: Game, rating: int, user: User) -> dict:
        game_ownership = GameOwnership.objects.get(user=user, game=game)
        game_ownership.rating = rating
        game_ownership.save()
        serializer = GameOwnershipSerializer(game_ownership, many=False)
        message = {'message': f"{user.username} successfully rated {game.name}", 'result': serializer.data}
        return message


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=False, methods=["POST"])
    def start_session(self, request):
        session = Session()
        session.start = datetime.datetime.now()
        players = [player for player in request.data['players']]
        players.append(Player.objects.get(user=request.user))
        session.save()

        for player in players:
            link = PlayerSessionLink()
            link.player = player
            link.session = self
            link.save()
        return Response({"message": "Session started"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['PUT'])
    def end_session(self, request, pk):
        session = Session.objects.get(id=pk)
        session.end = datetime.datetime.now()
        session.save()
        return Response({"message": "Session ended"}, status=status.HTTP_202_ACCEPTED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserMiniSerializer
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance)
        return Response(serializer.data)


class GameOwnershipViewSet(viewsets.ModelViewSet):
    queryset = GameOwnership.objects.all()
    serializer_class = GameOwnershipSerializer
    authentication_classes = (TokenAuthentication,)


class PlayerSessionLinkViewSet(viewsets.ModelViewSet):
    queryset = PlayerSessionLink.objects.all()
    serializer_class = PlayerSessionLinkSerializer
    authentication_classes = (TokenAuthentication,)
