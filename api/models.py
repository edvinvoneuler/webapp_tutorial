from django.db import models


# Create your models here.

class Game(models.Model):
    # Attributes
    name = models.CharField(max_length=256, unique=True)
    steam_app_id = models.CharField(max_length=256, null=True, blank=True)

    # TODO: Think about how to implement this, will it be provided through Steam API calls? If not, too manual.
    # genre = models.ForeignKey(Genre)


class Session(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
