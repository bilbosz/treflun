from django.shortcuts import render
from .models import Token


def index(request):
    return render(request, 'game/gameboard.html', {'token_list': Token.objects.all()})
