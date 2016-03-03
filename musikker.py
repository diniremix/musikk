#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse, sys, os, urllib2, json

from collections import namedtuple

URL_BASE = 'https://api.spotify.com/v1/search?q='

if sys.platform.startswith('linux'):
    os.system('clear')
elif sys.platform.startswith('win'):
    os.system('cls')

def handleRequest(stream):
    req = stream.read()
    # resp = json.loads(req)

    obj = json.loads(req, object_hook=lambda d: namedtuple('musikker', d.keys())(*d.values()))

    print 'Artist:', obj.tracks.items[0].artists[0].name
    print 'Album:', obj.tracks.items[0].album.name
    print 'Track:', obj.tracks.items[0].name
    print 'Spotify uri:', obj.tracks.items[0].uri

request = urllib2.Request(URL_BASE+'track:lacrymosa%20artist:evanescence&type=track&limit=1')
opener = urllib2.build_opener()
print 'getting json data...'

try:
    stream = opener.open(request)
    handleRequest(stream)
except urllib2.HTTPError as e:
    print 'Error:', e.code, 'the url:', e.url, e.reason
except urllib2.URLError as e:
    print 'Error with the url:', e.reason
