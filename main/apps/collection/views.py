from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from .models import Collection, Collection_has_games
from .forms import SearchForm
import json,urllib

# Create your views here.
def collection(request):
    # collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    # collection = serializers.serialize('json', collection)
    # collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    # collection_has_games = serializers.serialize('json', collection_has_games)
    collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    print(collection)
    return render(request,
                  'dashboard/dashboard.html',
                  {'collection_has_games':collection_has_games,
                   'collection':collection,})


@csrf_exempt
def collection_view(request):
    collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection = serializers.serialize('json', collection)
    collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection_has_games = serializers.serialize('json', collection_has_games)
    if request.is_ajax():
        if request.method == "POST":
            data = request.POST.get('colToDelete')
            print(data)
            Collection.objects.filter(collection_name=data).delete()
            Collection_has_games.objects.filter(collection_name=data).delete()
            Collection_has_games().save()
            Collection().save()
        if request.method == "GET":
            data = request.GET.getlist('gamesToDelete[]')
            for i in data:
                Collection_has_games.objects.filter(pk=i).delete()
            Collection_has_games().save()
    return render(request,
                  'dashboard/collection.html',
                  {'collection_has_games':collection_has_games,
                   'collection':collection,})

@csrf_exempt
def search(request):
    searchquery = ''
    collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection = serializers.serialize('json', collection)
    collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection_has_games = serializers.serialize('json', collection_has_games)
    #get ajax data
    if request.is_ajax() and request.method == "POST":
        data = request.POST.get("new_col[]","")
        Collection.objects.create(user_id=request.user.id,collection_name=data)
        Collection().save()

    if request.is_ajax() and request.method == "GET":
        #parse json file into python dictionary
        data = {k:v[0] for k,v in dict(request.GET).items()}
        #six values per game, will increment accordingly
        processed_data = {}
        i = 0
        for key,value in data.items():
            if "game" in key:
                i+=1
                processed_data[i] = {}
            k = key[1:].replace("[","").replace("]","")
            processed_data[i][k] = value
        if not (Collection.objects.filter(collection_name=processed_data[i]["collection_name"]).exists()):
            Collection.objects.create(user_id=int(processed_data[1]['userId']),
                                      collection_name=processed_data[1]['collection_name'])
        for ind in processed_data:
            game = processed_data[ind]
            print("data is here: ",str(game))
            Collection_has_games.objects.create(user_id=game["userId"],
                                                collection_name=game["collection_name"],
                                                game_id=game["id"],
                                                game_name=game["game"],
                                                photo=game["image"],
                                                rating=game["rating"],
                                                difficulty=game["complexity"])
        Collection().save()
        Collection_has_games().save()
    if request.method == "POST":
        fb = request.POST.get('fcal',False)
        searchquery = fb
    return render(request,
                  'dashboard/search.html',
                  {'searchquery':searchquery,
                  'collection':collection,
                  'collection_has_games':collection_has_games,})


def new(request):
    return HttpResponse('New Collection')
