'''INSERT INTO forum_forum("created","updated","name","slug","link_redirects","link_redirects_count","type","tree_id","level","parent_id","display_sub_forum_list","lft","rght","direct_posts_count","direct_topics_count","display_sub_forum_list","description_rendered")
SELECT datetime(),datetime(),"details.name",REPLACE(REPLACE(REPLACE(REPLACE(REPLACE("details.name",
' ','-'),
'.',''),
'/',''),
':',''),
';',''),0,0,0,2,2,5,1,0,0,0,0,1,"<p></p>",
FROM BoardGames
WHERE "attributes.boardgamefamily" LIKE "%CCG%";'''

import sqlite3
lft = 1
rght = 2
connection  = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

table_query = "SELECT * FROM forum_forum"

cursor.execute(table_query)
tableList = cursor.fetchall()

# print(tableList[3][0])

connection  = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
for i in range(0,len(tableList)):
    quer = "UPDATE forum_forum SET lft=" + str(lft) + ", rght=" + str(rght) + " WHERE id=" + str(tableList[i][0])
    cursor.execute(quer)
    lft+=2
    rght+=2

connection.commit()
print("done")
