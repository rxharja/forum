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


def get_distance(game_name,factor,dataframe):
    similarity = []
    category = dataframe.lookup(dataframe[dataframe['details.name'] == game_name].index,[factor])
    for index,row in dataframe.iterrows():
        if str(row[factor]) != '':
            distance = Levenshtein.distance(','.join(category),str(row[factor]))
            similarity.append(str(distance))
    return similarity 
    

def create_similarity_matrix(dataframe,filename,game_name,factor1='attributes.boardgamefamily',factor2='attributes.boardgamecategory',factor3='attributes.boardgamemechanic'):
    similarity1 = get_distance(game_name,factor1,dataframe)
    similarity2 = get_distance(game_name,factor2,dataframe)
    similarity3 = get_distance(game_name,factor3,dataframe)
    mean_similarity = [game_name]
    for i in range(len(similarity1)):
        mean = int (similarity1[i]+similarity2[i]+similarity3[i]) / 3
        mean_similarity.append(str(mean))
    file = open(filename,'a')
    file.write(','.join(mean_similarity))
    file.write('\n')
    file.close()
    
#create the matrix for the first 20 games
#test:
#create_similarity_matrix(df,'game_similarity.csv','Die Macher')
    
counter = 0
for index2,row2 in df.iterrows():
    if counter <= 20:
        #print(type(row2['details.name']))
        create_similarity_matrix(df,'game_similarity.csv',row2['details.name'])
        counter += 1
    