import sqlite3
import api
import simplejson
import logging

def create_table():

    '''
    Create db and table
    '''
    with sqlite3.connect('links.db') as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS ReadLater(key INTEGER PRIMARY KEY, link TEXT, title TEXT, read_state INT);')

def add_rows_in_table():
    '''
    Add rows in local storage
    '''
    data = api.retrive_list({"state" : "all"})
    ls = simplejson.loads(data)
    ls = ls['list'].values()
    rows = list()
    for ll in ls:
        key = ll.get('item_id')
        link = ll.get('resolved_url')
        title = ll.get('resolved_title')
        state = ll.get('status')
        print(key + " " + link + " " + title + " " + state)
        rows.append([key, link, title, state])

    with sqlite3.connect('links.db') as con:
        cur = con.cursor()
        # insert_statement = 'INSERT INTO ReadLater values(' + key + ', "' + link + '", "' + title + '", ' + state + ')'
        insert_statement = 'insert or replace into ReadLater values(?, ?, ?, ?)'
        cur.executemany( insert_statement , rows)
        con.commit()

def view_table():
    print("ID  URL  Title Read")
    with sqlite3.connect('links.db') as con:
        cur = con.cursor()
        for row in cur.execute("select * from ReadLater"):
            print(row)
        

