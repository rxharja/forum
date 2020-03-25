import psycopg2
import os
from django import template

register = template.Library()

@register.simple_tag
def search(game_query):
    if game_query == '':
        return "No Search";
    def search_game(game_query):
        try:
            con = psycopg2.connect(os.environ['DATABASE_URL'],sslmode='require')
            cursorObj = con.cursor()
            cursorObj.execute("SELECT \"details.name\",\"details.description\",\"stats.average\",\"stats.averageweight\",\"details.image\",\"game.id\" FROM boardgames WHERE LOWER(\"details.name\") like LOWER(\'%" + game_query + "%\') ORDER BY \"stats.usersrated\" DESC LIMIT 2500;")
            return cursorObj.fetchall()
        except:
            print("Sorry no database found for search_games!")
        finally:
            con.close()

    games = search_game(game_query)
    search_dict = {}
    k = 0
    for game in games:
        search_dict[k] = {}
        search_dict[k]["game"] = game[0]
        # search_dict[k]["description"] = game[1]
        search_dict[k]["rating"] = round(game[2],1)
        search_dict[k]["complexity"] = round(game[3],1)
        search_dict[k]["image"] = game[4]
        search_dict[k]["id"] = game[5]
        k+=1

    return search_dict
