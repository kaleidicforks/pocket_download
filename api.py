import simplejson
import httplib2
import urllib
import keys

import simplejson

consumer_key = keys.consumer_key
code = keys.code
my_token = keys.my_token

def get_token():
    '''
    Testing code,
    '''
    dc = dict()
    dc['consumer_key'] = consumer_key
    dc['reditect_uri'] = ''
    params = urllib.urlencode(dc)
    url = 'https://getpocket.com/v3/oauth/request'

    h = httplib2.Http(".cache") 
    resp, content = h.request( uri = retrieve_url, method = "POST", body = data, headers = headers)

    print content


def authorise():
    import simplejson
    headers = dict()
    headers['Content-Type'] = 'application/json; charset=UTF-8'
    headers['X-Accept'] = 'application/json'

    dc = dict()
    retrieve_url = "https://getpocket.com/v3/oauth/authorize" 
    dc['consumer_key'] = consumer_key
    dc['code'] = code
    data = simplejson.dumps(dc)
    h = httplib2.Http(".cache") 
    resp, content = h.request( uri = retrieve_url, method = "POST", body = data, headers = headers)
    print content


def retrive_list(dc = {}, token = None):
    if not token:
        token = my_token
    headers = dict()
    headers['Content-Type'] = 'application/json; charset=UTF-8'
    headers['X-Accept'] = 'application/json'

    retrieve_url = "https://getpocket.com/v3/get" 
    dc['consumer_key'] = consumer_key
    dc['access_token'] = token
    data = simplejson.dumps(dc)
    h = httplib2.Http(".cache") 
    resp, content = h.request( uri = retrieve_url, method = "POST", body = data, headers = headers)
    return content

def add_to_list(url_to_add):
    '''
    Pass a link to add to list
    '''
    token = my_token
    headers = dict()
    headers['Content-Type'] = 'application/json; charset=UTF-8'
    headers['X-Accept'] = 'application/json'

    dc = dict()
    retrieve_url = "https://getpocket.com/v3/add" 
    dc['consumer_key'] = consumer_key
    dc['access_token'] = token
    dc['url'] = url_to_add
    data = simplejson.dumps(dc)
    h = httplib2.Http(".cache") 
    resp, content = h.request( uri = retrieve_url, method = "POST", body = data, headers = headers)
    print content

def analayse_data():
    '''
    Analyse data
    '''
    # Get all unread data
    dc = dict()
    dc['state'] = 'unread'
    data = retrive_list(dc)
    ls = simplejson.loads(data)
    ls = ls['list'].values()
    count_unread = len(ls)
    total_ur_words = 0
    for ll in ls:
        total_ur_words += int(ll.get('word_count', 0))
        print ll.get('resolved_url')

    # Get all archive data
    dc = dict()
    dc['state'] = 'archive'
    data = retrive_list(dc)
    ls = simplejson.loads(data)
    ls = ls['list'].values()
    count_archive = len(ls)
    total_read_words = 0
    for ll in ls:
        total_read_words += int(ll.get('word_count', 0))

    print "Total unread articles " + str(count_unread)
    print "Total read articles " + str(count_archive)
    print "Total unread words " + str(total_ur_words)
    print "Total read words " + str(total_read_words)








