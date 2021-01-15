from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.ForeignKey(User, models.deletion.DO_NOTHING)

    def __str__(self):
        return str(self.user)


class Map(models.Model):
    name = models.CharField(default="", max_length=64)
    image = models.ImageField(default="default_map.png", upload_to="maps")

    maps = models.Manager()

    def __str__(self):
        return str(self.name)


class Token(models.Model):
    name = models.CharField(default="", max_length=64)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    owner = models.ForeignKey(Player, models.deletion.DO_NOTHING)
    image = models.ImageField(default="default.png", upload_to="tokens")

    def __str__(self):
        return str(self.name)
