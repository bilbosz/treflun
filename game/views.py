from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from game.models.Map import Map
from game.models.Token import Token


@login_required
def index(request):
    return render(request, 'index.html',
                  {'token_list': Token.objects.all(), 'map': Map.objects.get(id=1), 'user': request.user})
