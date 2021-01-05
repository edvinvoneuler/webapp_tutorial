from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    # Attributes
    name = models.CharField(max_length=256, unique=True)
    steam_app_id = models.CharField(max_length=256, null=True, blank=True)

    # TODO: Think about how to implement this, will it be provided through Steam API calls? If not, too manual.
    # genre = models.ForeignKey(Genre)


class Session(models.Model):
    # Attributes
    start = models.DateTimeField()
    end = models.DateTimeField()

    # Relationships
    game = models.ForeignKey(Game, on_delete=models.PROTECT)


class PlayerSessionLink(models.Model):
    # This is just here in case we want to add some attributes to this relationship, like session stats per player.
    # (plus its nicer to be explicit IMO)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session_player_links')
    player = models.ForeignKey('Player', on_delete=models.PROTECT, related_name='player_session_links')


class GameOwnership(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_ownership_link")
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name="player_ownership_link")
    rating = models.IntegerField(null=True, blank=True, choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])


class Player(models.Model):
    # Attributes
    nickname = models.CharField(max_length=256)

    # Relationships
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Session, through=PlayerSessionLink, related_name="participating_players")
    owned_games = models.ManyToManyField(Game, through=GameOwnership, related_name="players_owning")
