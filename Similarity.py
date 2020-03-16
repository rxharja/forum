#########################################
#                                       #
# A content-based recommendation system #
#  (based on catogory/family/mechanic)  #
#                                       #
#########################################
#(requires data preprocessing to make sure there's no empty cell)

# pip install python-Levenshtein
import pandas as pd
import Levenshtein
import operator

#read the csv file with game info
df = pd.read_csv('game_data.csv',sep=',', names=
                 ['game.id', 'details.name', 'attributes.boardgamecategory', 'attributes.boardgamefamily', 'attributes.boardgamemechanic', 'stats.average', 'details.playingtime'])
#delete the first row, which is the header name
df = df.iloc[1:,]
df.set_index('game.id')
#df.head()
#df.describe()

#test Levenshtein distance
#distance = Levenshtein.distance('abc','abd')
#print(distance)

#a = df.lookup(df[df['details.name']=='Die Macher'].index,['attributes.boardgamecategory'])
#type(a)


def get_distance(game_id,factor,dataframe):
    similarity = []
    category = dataframe.lookup(dataframe[dataframe['game.id'] == game_id].index,[factor])
    for index,row in dataframe.iterrows():
        if str(row[factor]) != '' or str(row[factor]) != 'Admin: Better Description Needed!':
            distance = Levenshtein.distance(','.join(category),str(row[factor]))
            similarity.append(str(distance))
    return similarity 
     
  
def create_similarity_matrix(dataframe,filename,game_id,factor1='attributes.boardgamefamily',factor2='attributes.boardgamecategory',factor3='attributes.boardgamemechanic'):
    similarity1 = get_distance(game_id,factor1,dataframe)
    similarity2 = get_distance(game_id,factor2,dataframe)
    similarity3 = get_distance(game_id,factor3,dataframe)
    mean_similarity = [game_id]
    print(game_id)
    for i in range(len(similarity1)):
        mean = int (similarity1[i]+similarity2[i]+similarity3[i]) / 3
        mean_similarity.append(str(mean))
    file = open(filename,'a')
    file.write(','.join(mean_similarity))
    file.write('\n')
    file.close()
    
#create the matrix for the first 20 games
#test:
#create_similarity_matrix(df,'game_similarity.csv','Samurai')
#create_similarity_matrix(df,'game_similarity.csv',8)
    
counter = 0
for index2,row2 in df.iterrows():
    if counter < 20:
        #print(type(row2['details.name']))
        #print(row2['details.name'])
        try:
            print('analysing',row2['game.id'])
            create_similarity_matrix(df,'game_similarity.csv',row2['game.id'])
        except:
            print('error occurs at', row2['game.id'])
        counter += 1
        
def get_most_similar_game(game_id,similarity_file,info_file_df):
    df = pd.read_csv(similarity_file,sep=',',header=None)
    row_index = df[df[0] == game_id].index
    row = df.loc[row_index]
    row = row.values.tolist()
    new_row = row[1:,]
    s_dict = {}
    counter = 1
    for i in new_row:
        s_dict[counter]=i
        counter += 1
    sorted_dict = sorted(s_dict.items(), key=operator.itemgetter(1))
    game_id = sorted_dict[1]
    game_name = info_file_df.lookup(info_file_df[info_file_df['game.id'] == game_id].index,['details.name'])
    return game_name
    
name = get_most_similar_game(1,"game_similarity.csv",df)
print (name)

##test:
dff = pd.read_csv('game_similarity.csv',sep=',',header=None)
dff.head()
row_index = dff[dff[0] == 2].index
row = dff.loc[row_index]
row = row.values.tolist()
print(row)
new_row = row[1:,]