from django.shortcuts import render

from .models import Token, Map


def index(request):
    return render(request, 'index.html',
                  {'token_list': Token.objects.all(), 'map': Map.maps.get(id=1), 'user': request.user})
