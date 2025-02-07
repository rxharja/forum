# import seaborn as sns
# import matplotlib.pyplot as plt
from main.apps.collection.templatetags.get_from_db import get_from_db
import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django import template

register = template.Library()

'''
Handles the creation of the similarity matrix and the retrieving

of the five most similar games to a user. It will return 5 similar games based
on a game a user has subscribed to in the board games, has posted the most in,
or has owned in a collection.

inputs:
id: int based on user id
'''

@register.simple_tag
def similarity(id):
    ''' Variables to change  '''
    # game to check similarity
    user_id = id
    # file to save cosine similarity matrix as to not build it again
    matrix_file = "./similarity_matrix.csv"

    # create list of important columns to keep
    features = ['attributes.boardgamecategory',
                'attributes.boardgamefamily',
                'attributes.boardgamemechanic',
                'attributes.boardgamepublisher',
                'attributes.boardgamedesigner',
                'attributes.boardgameartist']

    # keywords pertaining to expansions
    # expansions = ['game.type',
    #               'attributes.boardgameexpansion']

    ''' Functions  '''
    # helper function to get title from index
    def get_title_from_index(index):
        return df[df['index'] == index]['details.name'].values[0]

    # helper function to get index from title
    def get_index_from_title(title):
        return df[df['details.name'] == title]['index'].values[0]

    def get_weight_from_index(index):
        return df[df['index'] == index]['stats.averageweight'].values[0]

    def get_rating_from_index(index):
        return df[df['index'] == index]['stats.average'].values[0]

    def get_description_from_index(index):
        return df[df['index'] == index]['details.description'].values[0]

    def get_image_from_index(index):
        return df[df['index'] == index]['details.image'].values[0]

    # queries views user_most_posted forum and user_subscribed_games to make a list of tuples
    # each tuple is ("posted or subscribed",name of game)
    def get_board_most_posted(user_id):
        games_to_rec = []
        try:
            query = "SELECT name FROM user_most_posted_game WHERE id=" + str(user_id)
            most_posted = get_from_db(query, 'one')
            if most_posted:
                games_to_rec.append(('posted', most_posted[0]))
        except RuntimeError:
            print("user_most_posted_game table not found!")

        try:
            query = "SELECT name FROM user_subscribed_games WHERE id=" + str(user_id)
            recs = get_from_db(query, 'all')
            for game in recs:
                games_to_rec.append(('subscribed', game[0]))
        except:
            print("user_subscribed_games not found!")

        try:
            query = "SELECT game_name FROM collection_collection_has_games WHERE user_id=" + str(user_id)
            cols = get_from_db(query, 'all')
            for game in cols:
                games_to_rec.append(('owned', game[0]))
            # print(games_to_rec)
        except:
            print("collection database not found!")

        finally:
            return games_to_rec

    # import boardgames table from sql database and return it as a pandas dataframe
    def get_table_from_sqlite():
        try:
            query = '''SELECT * FROM boardgames
                       WHERE "stats.usersrated"!=0
                       AND "game.type"='boardgame'
                       ORDER BY "stats.usersrated" DESC
                       LIMIT 2500;'''
            df = get_from_db(query,'all',to_pd=True)
            # numbers in incremental order needed to cosine similarity matrix to work
            df['index']=df.index
            # clean and process data first
            for feature in features:
                df[feature] = df[feature].fillna('') # filling missing vals with empty str
            # apply the function to each row in data set to store the combined strings into column called combined_features
            df['combined_features'] = df.apply(combine_features, axis=1)
            return df
        except RuntimeError:
            print("Sorry, database not found!")

    # combine values of important columns into a single string
    def combine_features(row):
        # this abstracted way gives different results in matrix
        # combined_features = ''
        # for feature in features:
        #     combined_features += row[feature] + ' '
        # return combined_features.rstrip(' ')

        return row['attributes.boardgamecategory'] + ' '
        + row['attributes.boardgamefamily'] + ' '
        + row['attributes.boardgamemechanic'] + ' '
        + row['attributes.boardgamepublisher'] + ' '
        + row['attributes.boardgamedesigner'] + ' '
        + row['attributes.boardgameartist']

    def get_matrix():
        try:
            matrix_df = pd.read_csv(matrix_file, delimiter=",", header=None, index_col=False)
            return [list(row) for row in matrix_df.values]
        except IOError:
            # convert collection of text  to matrix of token counts
            count_matrix = CountVectorizer().fit_transform(df['combined_features'])
            # get cosine similarity matrix from count matrix
            cosine_sim = cosine_similarity(count_matrix)
            # export cosine similarity matrix as csv
            pd.DataFrame(cosine_sim).to_csv(matrix_file, header=False, index=False)
            return cosine_sim

    # import table from sql database
    df = get_table_from_sqlite()
    print(df)
    rec_games_list = []
    # import game user likes from sql database
    rec_games_list.extend(get_board_most_posted(user_id))
    rand_num = random.randint(0,100)
    if rec_games_list == [] or rand_num <= 10:
        rec_game = ("random",get_title_from_index(random.randrange(0,len(df))))
    else:
        rec_game = random.choice(rec_games_list)
    # add a wildcard
    # rec_games_list.append( ("random", get_title_from_index( random.randrange(0,len(df)))))
    why_recommended = rec_game[0]
    game_user_likes = rec_game[1]
    print(rec_game, rec_games_list)
    # import cosine similarity matrix
    cosine_sim = get_matrix()

    # Find that movies index
    game_index = get_index_from_title(game_user_likes)
    # print(game_index)

    # enumerate through similarity scores of the game_user_likes variable
    # return tuple of game index and similarity scores in the form (game id,similarity score)
    similar_games = list(enumerate(cosine_sim[game_index]))
    # print(similar_games)
    # sort list of similar games according to similarity scores in descending order, skip the first element because thats the game itself
    sorted_similar_games = sorted(similar_games,
                                  key=lambda x: x[1], reverse=True)[1:]
    # print(sorted_similar_games)

    # show top 5 most similar entries
    i = 0
    # data to push to sql database keeping track of recommendations
    # games_to_recommend = [user_id,game_user_likes]
    recommended_games_dict = {}
    # games we plan not not recommending to user based on their patterns
    games_to_skip = [game[1] for game in rec_games_list]
    print("Because you liked " + game_user_likes + "...\n")
    for game in sorted_similar_games:
        game_dict = {}
        game_dict["user"] = user_id
        game_dict["based_on"] = game_user_likes
        if i > 4:
            break
        # Games that are already post a lot about or own should be removed
        # We filter those games here
        if (get_title_from_index(game[0]) != game_user_likes) \
                and (get_title_from_index(game[0]) not in games_to_skip):
            # games_to_recommend.append(get_title_from_index(game[0]))
            game_dict["game"] = get_title_from_index(game[0])
            # game_dict["description"] = get_description_from_index(game[0])
            game_dict["difficulty"] = str(round(get_weight_from_index(game[0]), 1)) + "/5"
            game_dict["rating"] = str(round(get_rating_from_index(game[0]), 1)) + "/10"
            game_dict["image"] = get_image_from_index(game[0])
            recommended_games_dict[i] = game_dict
            i += 1

    return why_recommended, recommended_games_dict
