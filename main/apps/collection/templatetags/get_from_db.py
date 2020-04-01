from project.settings.base import DATABASES
import psycopg2
import sqlite3
import os
import pandas as pd

'''
get_from_db
certain tables in the database are not hooked up to the django model,
for example, the game database table as it was taken from kaggle.
This manages accessing those tables and views based on the two tables
supported by this app, postgres and sqlite3 ones.

inputs:
query = sql string
amount = one or all, one retrieves 1 hit, all retrieves all
to_pd = import the results as a pandas dataframe
'''

def get_from_db(query, amount, to_pd=False):

    # default is to try accessing postgres
    try:

        # get default database engine from the settings
        default = DATABASES['default']['ENGINE']
        print("working with the", default, "database")

        # if the default is a postgres database,
        # check if the app is on heroku, as heroku defaults to postgres,
        if default == 'django.db.backends.postgresql_psycopg2':
            try:
                # heroku requires using os.environ to get the database url
                con = psycopg2.connect(os.environ['DATABASE_URL'],
                                       sslmode='require')
            # 'DATABASE_URL' will throw an error if its not heroku, so
            # default to local postgres database
            except KeyError:
                con = psycopg2.connect(dbname=DATABASES['postgresql']['NAME'],
                                       port='5432')
        # if the database is not postgres, its a local sqlite3 one
        else:
            con = sqlite3.connect(DATABASES['mysql']['NAME'])

        # connect set up the cursor object based on the con
        cursorObj = con.cursor()

        # if we want to return a dataframe, return at this point
        if to_pd:
            return pd.read_sql_query(query, con)

        else:
            # otherwise, we execute our query and return one or all
            cursorObj.execute(query)
            if amount == "all":
                return cursorObj.fetchall()
            elif amount == "one":
                return cursorObj.fetchone()
            else:
                print("improper amount of queries to get chosen")
    except:
        print("database error")
    finally:
        # close the connection
        con.close()
