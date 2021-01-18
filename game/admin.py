from django.contrib import admin

from game.models.Map import Map
from game.models.Player import Player
from game.models.Token import Token

admin.site.register(Map)
admin.site.register(Player)
admin.site.register(Token)
