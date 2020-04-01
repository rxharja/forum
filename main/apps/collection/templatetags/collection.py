#import template to use as tag in HTML
from django import template
#import script to handle talking to database and retrieving information
from main.apps.collection.templatetags.get_from_db import get_from_db

register = template.Library()

'''
!!! This tag isn't being used since these two tables are accessed by the
django model now, but the file is staying here for documentation purposes

Takes a user id and returns a dictionary of the user's
collections. Each collection has a dictionary containing the first game's
name and image.

inputs:
user_id: integer
'''

@register.simple_tag
def one_collection(user_id):
    # return all collection names associated with a user
    def get_collections(user_id):
        get_from_db("SELECT collection_name \
                     FROM collection_collection \
                     WHERE user_id ="+str(user_id), 'all')

    # Get first hit from collection details
    # based on collection name and user id as
    # multiple users may have collections with the same name
    def get_collection_details(name, user_id):
        get_from_db('SELECT * \
                     FROM user_collections \
                     WHERE collection_name = \"' + name + '\" \
                     AND user_id='+str(user_id), 'one')

    # get all collections a user has made
    query = get_collections(user_id)
    cols = {}

    k = 0
    # loop through user's collections
    # build a dictionary like so:
    # {index: {'name': 'collection name', 'image': ''}}
    # each collection has one game and one image associated with it
    for col in query:
        cols[k] = {}
        col_deets = get_collection_details(col[0], user_id)
        cols[k]['name'] = col_deets[1]
        cols[k]["image"] = col_deets[4]
        k += 1

    return cols
