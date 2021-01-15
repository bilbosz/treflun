from django.shortcuts import render

from .models import Token


def index(request):
    return render(request, 'index.html', {'token_list': Token.objects.all(), 'user': request.user})
