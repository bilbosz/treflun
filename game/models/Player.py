from django.contrib.auth.models import User
from django.db import models

from game.managers.PlayerManager import PlayerManager


class Player(models.Model):
    user = models.ForeignKey(User, models.deletion.DO_NOTHING)

    objects = PlayerManager

    def __str__(self):
        return str(self.user)
