from django import template
from main.apps.collection.templatetags.get_from_db import get_from_db

register = template.Library()


@register.simple_tag
def one_collection(user_id):

    def get_collections(user_id):
        get_from_db("SELECT collection_name \
                     FROM collection_collection \
                     WHERE user_id ="+str(user_id), 'all')

    def get_collection_details(name, user_id):
        get_from_db('SELECT * \
                     FROM user_collections \
                     WHERE collection_name = \"' + name + '\" \
                     AND user_id='+str(user_id), 'one')

    query = get_collections(user_id)
    cols = {}

    k = 0
    for col in query:
        cols[k] = {}
        col_deets = get_collection_details(col[0], 1)
        cols[k]['name'] = col_deets[1]
        cols[k]["image"] = col_deets[4]
        k += 1

    return cols
