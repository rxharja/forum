import sqlite3
from django import template

register = template.Library()

@register.simple_tag
def top_collections(user_id):
    def get_collections(user_id):
        try:
            con = sqlite3.connect("db.sqlite3")
            cursorObj = con.cursor()
            cursorObj.execute("SELECT collection_name FROM collection_collection WHERE user_id =="+str(user_id))
            return cursorObj.fetchall()
        except:
            print("Sorry database not found!")
        finally:
            con.close()

    def get_collection_details(name,user_id):
        try:
            con = sqlite3.connect("db.sqlite3")
            cursorObj = con.cursor()
            cursorObj.execute('SELECT * FROM collection_collection_has_games WHERE collection_name == \"'+ name + '\" AND user_id=='+str(user_id)+ ' LIMIT 6')
            return cursorObj.fetchall()
        except:
            print("Sorry database not found!")
        finally:
            con.close()

    query = get_collections(user_id)
    if query == []: return None

    cols = {}

    for col in query:
        col_deets =get_collection_details(col[0],user_id)
        if col_deets:
            col_id = col_deets[0][0]
            i = 0
            cols[col_id] = {}
            print(cols)
            for entry in col_deets:
                cols[col_id][i] = {}
                cols[col_id][i].update({'col_name':entry[6],
                                        'game_name':entry[7],
                                        'image':entry[4]})
                i+=1

    print(cols)
    return cols
