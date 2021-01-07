from rest_framework import serializers

from api.models import Game, GameOwnership, Session, PlayerSessionLink
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'steam_app_id', 'no_of_owners', 'avg_rating']


class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class GameOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameOwnership
        fields = ['id', 'user', 'game', 'rating']


class SessionSerializer(serializers.ModelSerializer):
    users = UserMiniSerializer(many=True)

    class Meta:
        model = Session
        fields = ['id', 'game', 'users', 'start', 'end']


class PlayerSessionLinkSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(many=False)

    class Meta:
        model = PlayerSessionLink
        fields = ['user', 'session']


class UserSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)
    owned_games = GameSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'owned_games', 'sessions', 'username']
