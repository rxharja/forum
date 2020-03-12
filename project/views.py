from django.shortcuts import render
from machina import urls as machina_urls

def home(request):
    return render(request,machina_urls);
