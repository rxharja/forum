from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.
def games(request):
    game = Game.objects.all()
    return render(request, 'recommendations/recommendations.html',
                            {'game':game})

def new(request):
    return HttpResponse('New Game')
