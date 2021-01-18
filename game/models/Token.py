from django.db import models

from game.managers.TokenManager import TokenManager
from game.models.Player import Player


class Token(models.Model):
    name = models.CharField(default="", max_length=64)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    owner = models.ForeignKey(Player, models.deletion.DO_NOTHING)
    image = models.ImageField(default="default.png", upload_to="tokens")

    objects = TokenManager

    def canMove(self):
        pass

    def __str__(self):
        return str(self.name)
