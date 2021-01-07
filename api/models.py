from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    # Attributes
    name = models.CharField(max_length=256, unique=True)
    steam_app_id = models.CharField(max_length=256, null=True, blank=True)

    owning_users = models.ManyToManyField(User, through='GameOwnership', related_name="owned_games")
    # TODO: Think about how to implement this, will it be provided through Steam API calls? If not, too manual.
    # genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.name

    def no_of_owners(self):
        owned_by = GameOwnership.objects.filter(game=self)
        return len(owned_by)

    def avg_rating(self):
        ownerships = GameOwnership.objects.filter(game=self)
        no_ratings = 0
        rating_sum = 0
        for ownership in ownerships:
            if ownership.rating is not None:
                rating_sum += ownership.rating
                no_ratings += 1
        return rating_sum / len(ownerships) if no_ratings != 0 else 0


class Session(models.Model):
    # Attributes
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    users = models.ManyToManyField(User, through='PlayerSessionLink', related_name="sessions")

    # Relationships
    game = models.ForeignKey(Game, on_delete=models.PROTECT)


class PlayerSessionLink(models.Model):
    # This is just here in case we want to add some attributes to this relationship, like session stats per player.
    # (plus its nicer to be explicit IMO)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session_player_links')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_session_links')

    class Meta:
        unique_together = (('user', 'session'),)


class GameOwnership(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_ownership_link")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ownership_link")
    rating = models.IntegerField(null=True, blank=True, choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])

    class Meta:
        unique_together = (('user', 'game'),)


# class Player(models.Model):
#     # Attributes
#     nickname = models.CharField(max_length=256)
#
#     # Relationships
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     sessions = models.ManyToManyField(Session, through=PlayerSessionLink, related_name="participating_players")
#     owned_games = models.ManyToManyField(Game, through=GameOwnership, related_name="players_owning")
#
#     def __str__(self):
#         return f"{self.user.username} : {self.nickname}"
