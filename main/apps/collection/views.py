from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from .models import Collection, Collection_has_games
from .forms import SearchForm
import json,urllib

# Create your views here.

def collection(request):
    # filter collections by user where theres no empty values, for some reason
    # multiple empty values get created sometime, not sure why
    collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    # print(collection)
    return render(request,
                  'dashboard/dashboard.html',
                  {'collection_has_games':collection_has_games,
                   'collection':collection,})

# for the purposes of this prototype, csrf_exempt is being used
@csrf_exempt
def collection_view(request):
    '''
    handles the viewing and managing of a user's collection
    '''
    # filter collections and collection_has_games by user id, turn them into json
    # these will be returned to the template so we can use JS to work with the data
    collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection = serializers.serialize('json', collection)
    collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection_has_games = serializers.serialize('json', collection_has_games)

    if request.is_ajax():
        # if POST method detected, we're deleting a collection
        if request.method == "POST":
            # colToDelete is the name of the collections the user
            # wishes to delete, its just one at a time
            data = request.POST.get('colToDelete')
            # print(data)
            # delete the collections from the database for the name of the collection
            # make sure to include user id to not include other users collection
            Collection.objects.filter(collection_name=data,user_id=request.user.id).delete()
            Collection_has_games.objects.filter(collection_name=data,user_id=request.user.id).delete()
            Collection_has_games().save()
            Collection().save()
        # if GET method detected, we're deleting one game from the collection
        if request.method == "GET":
            # potentially could be multiple from one collection, so we expect a list
            # of the game's id in the collection
            data = request.GET.getlist('gamesToDelete[]')

            for i in data:
                Collection_has_games.objects.filter(pk=i,user_id=request.user.id).delete()
            Collection_has_games().save()
    return render(request,
                  'dashboard/collection.html',
                  {'collection_has_games':collection_has_games,
                   'collection':collection,})

@csrf_exempt
def search(request):
    '''
    handles the adding of selected games retrieved from a search to a user's
    chosen collection
    '''
    searchquery = ''
    collection = Collection.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection = serializers.serialize('json', collection)
    collection_has_games = Collection_has_games.objects.filter(user_id__isnull=False,user_id=request.user.id)
    collection_has_games = serializers.serialize('json', collection_has_games)
    #get ajax data
    if request.is_ajax() and request.method == "POST":
        # If its a POST request, we're creating a new empty collection for the user
        # on his or her id.
        data = request.POST.get("new_col[]","")
        Collection.objects.create(user_id=request.user.id,collection_name=data)
        Collection().save()

    if request.is_ajax() and request.method == "GET":
        #GET method used to add game to the chosen collection

        #parse json file into python dictionary
        data = {k:v[0] for k,v in dict(request.GET).items()}
        #six values per game, will increment accordingly
        processed_data = {}
        i = 0
        # build the dictionary based on each game, process appropriately for
        # storage
        for key,value in data.items():
            if "game" in key:
                i+=1
                processed_data[i] = {}
            k = key[1:].replace("[","").replace("]","")
            processed_data[i][k] = value

        # This was used when a user could type in their collection name to add it
        # could potentially use later since its an easy way to add to a collection
        # if not (Collection.objects.filter(collection_name=processed_data[i]["collection_name"]).exists()):
        #     Collection.objects.create(user_id=int(processed_data[1]['userId']),
        #                               collection_name=processed_data[1]['collection_name'])

        # add each game to the collection_has_games database based on the name
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

    # handles returning search queries to template
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
