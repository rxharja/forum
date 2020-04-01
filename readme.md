Forum with Games Similarity Recommendation System and Collection Management

Live version on Heroku:
https://young-wildwood-67631.herokuapp.com/

This app was built with django and the forum django-machina framework.
Scipy was used to for its count vectorizer and cosine similarity matrix building powers to create the games similarity matrix.

The games were taken from BoardGameGeek's boardgame database which can be found on kaggle here: https://www.kaggle.com/mandshaw/games-0918

The django-machina example was extended with a dashboard feature which allows a user to

manage their games collection,
search for new games,
view recommended games based on


a. forum activity:

most posted games forum
games forum subscriptions


b. their collection

games will be recommended based on what games a user owns in his or her collection



To view forum posts and the dash board, first make sure to log in, otherwise nothing will display. Then, click your username at the top right, and click the dashbaord button.
The games table in the database and some views are not hooked up to the django model because of its sheer size, so a sample sqlite3 database has been included to play around with already populated. The app also supports postgres, if you wish to use that instead.
