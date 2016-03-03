#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse, sys, os, urllib2, json, urllib
from collections import namedtuple

URL_BASE = 'https://api.spotify.com/v1/search?'

if sys.platform.startswith('linux'):
    os.system('clear')
elif sys.platform.startswith('win'):
    os.system('cls')

def handleRequest(stream):
    req = stream.read()
    # the magic!
    obj = json.loads(req, object_hook=lambda d: namedtuple('musikker', d.keys())(*d.values()))

    print 'Done!'
    print 'Artist:', obj.tracks.items[0].artists[0].name
    print 'Album:', obj.tracks.items[0].album.name
    print 'Track:', obj.tracks.items[0].name
    print 'Spotify uri:', obj.tracks.items[0].uri

def setParams(query):
    config = {
        'q': 'track:'+query['track']+' artist:'+query['artist'],
        'type': 'track',
        'limit': query['limit'] or 1
    }
    return config

def search():
    query={
        'artist':'evanescence',
        'track':'tourniquet',
        'limit':1
    }

    params= setParams(query)
    request= URL_BASE + urllib.urlencode(params)

    print 'searching track: "%s" of Artist: "%s"' % (query['track'], query['artist'])

    try:
        response = urllib2.urlopen(request)
        handleRequest(response)
    except urllib2.HTTPError as e:
        print 'Error:', e.code, 'the url:', e.url, e.reason
    except urllib2.URLError as e:
        print 'Error with the url:', e.reason

print 'getting json data...'
search()