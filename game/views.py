from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Token


@login_required
def index(request):
    return render(request, 'game/gameboard.html', {'token_list': Token.objects.all()})
