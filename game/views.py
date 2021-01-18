from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Token, Map


@login_required
def index(request):
    return render(request, 'game/gameboard.html', {'token_list': Token.objects.all(), 'map': Map.maps.get(id=1)})
