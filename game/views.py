from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
# Create your views here.
def index(request):
    game = Game.objects.all()
    return render(request, 'main.recommendations',
                            {'game':game})

def new(request):
    return HttpResponse('New Game')
