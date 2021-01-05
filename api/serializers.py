from rest_framework import serializers

from api.models import Player, Game, GameOwnership, Session, PlayerSessionLink


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'steam_app_id']


class PlayerMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']


class GameOwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameOwnership
        fields = ['id', 'player', 'game', 'rating']


class SessionSerializer(serializers.ModelSerializer):
    players = PlayerMiniSerializer(many=True)

    class Meta:
        model = Session
        fields = ['id', 'game', 'participating_players', 'start', 'end']


class PlayerSessionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSessionLink
        fields = ['player', 'game']


class PlayerSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)
    owned_games = GameSerializer(many=True)

    class Meta:
        model = Player
        fields = ['id', 'owned_games', 'sessions', 'name']
