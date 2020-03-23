import sqlite3
# from django import template
#
# register = template.Library()
#
# @register.simple_tag
# def top_collections(user_id):
def get_collections(user_id):
    try:
        con = sqlite3.connect("db.sqlite3")
        cursorObj = con.cursor()
        cursorObj.execute('SELECT "collection_name" FROM collection_collection WHERE user_id =='+str(user_id))
        return cursorObj.fetchall()
    except:
        print("Sorry not database found!")
    finally:
        con.close()

cols = get_collections(1)
print(cols)
