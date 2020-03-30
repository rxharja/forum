from project.settings.base import DATABASES
import psycopg2
import sqlite3
import os
import pandas as pd


def get_from_db(query, amount, to_pd=False):

    default = DATABASES['default']['ENGINE']
    if default == 'django.db.backends.postgresql_psycopg2':
        try:
            # web server heroku
            con = psycopg2.connect(os.environ['DATABASE_URL'],
                                   sslmode='require')
        except KeyError:
            con = psycopg2.connect(dbname=DATABASES['postgresql']['NAME'],
                                   port='5432')
    else:
        try:
            con = sqlite3.connect(DATABASES['mysql']['NAME'])
        except RuntimeError:
            return 'error!'
    cursorObj = con.cursor()

    try:
        if to_pd:
            return pd.read_sql_query(query, con)
        else:
            cursorObj.execute(query)
            if amount == "all":
                return cursorObj.fetchall()
            elif amount == "one":
                return cursorObj.fetchone()
            else:
                print("improper amount of queries to get chosen")
    except RuntimeError:
        print("Sorry! The query failed, check your syntax?")
        return ''
    finally:
        con.close()
