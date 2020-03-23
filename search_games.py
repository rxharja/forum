import sqlite3
# from django import template
#
# register = template.Library()
#
# @register.search_games
def search_game(game_query):
    try:
        con = sqlite3.connect("db.sqlite3")
        cursorObj = con.cursor()
        cursorObj.execute("SELECT \"details.name\",\"details.description\",\"stats.average\",\"stats.averageweight\" FROM BoardGames WHERE \"details.name\" like \"%" + game_query + "%\"")
        return cursorObj.fetchall()
    except:
        print("Sorry no database found!")
    finally:
        con.close()

games = search_game("infinity")
search_dict = {}
k = 0
for game in games:
    search_dict[k] = {}
    search_dict[k]['game'] = game[0]
    search_dict[k]['description'] = game[1]
    search_dict[k]['rating'] = game[2]
    search_dict[k]['complexity'] = game[3]
    k+=1

print(search_dict)
