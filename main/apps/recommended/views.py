from django.shortcuts import render
from django.http import HttpResponse
from .models import Recommended

# Create your views here.
def recommended(request):
    recommended = Recommended.objects.all()
    return render(request, 'recommendations/recommendations.html',
                            {'recommended':recommended})

def new(request):
    return HttpResponse('New Recommended')
