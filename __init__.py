#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:14:48 2018

@author: No_One
"""



import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

def TopArticles():
    print('__'*30) 
    c.execute('''SELECT ar.title, COUNT(*) as numar
        FROM articles as ar
        join log as lg
        ON lg.path LIKE concat('/article/%', ar.slug)
        GROUP BY ar.title
        ORDER BY numar DESC LIMIT 3;''')
    rslt = c.fetchall()
    for (title, view) in rslt:
        print("{} - {} views".format(title, view))
        
    print('__'*30)    


def TopAuthors():
    print('__'*30) 
    c.execute('''
        SELECT au.name, COUNT(*) as numau
        FROM authors as au
        join articles as ar 
        on  au.id = ar.author
        join log as lg
        ON SUBSTRING(lg.path, 10 ,30) like ar.slug
        GROUP BY au.name
        ORDER BY numau DESC;''')
    rslt = c.fetchall()

    for (name, view) in rslt:
        print("{} - {} views".format(name, view))
    print('__'*30)     


def DaysErrors():
    print('__'*30) 
    c.execute('''
        SELECT errview.date, round(100.0*errview.errview / totview.totview,2)
        as errors from totview , errview
        where errview.date=totview.date 
        and (errview.errview)>(totview.totview*0.01);''')
    rslt = c.fetchall()

    for (date, percentage) in rslt:
        print("    {} - {}% errview".format(date, percentage))
    print('__'*30)     

if __name__ == "__main__":
    TopArticles()
    TopAuthors()
    DaysErrors()