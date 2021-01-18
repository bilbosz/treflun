from django.db import models

from game.managers.MapManager import MapManager


class Map(models.Model):
    name = models.CharField(default="", max_length=64)
    image = models.ImageField(default="default_map.png", upload_to="maps")

    objects = MapManager

    def __str__(self):
        return str(self.name)
