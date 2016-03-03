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
    q=""
    if 'artist' in query:
        q = u'track:' + query['track'] + ' artist:' + query['artist']
    else:
        q = u'track:' + query['track']

    config = {
        'q': q,
        'type': 'track',
        'limit': query['limit'] or 1
    }
    return config

def loadList(filename):
    pass

def search(opts):
    query= {}
    if ':' in opts:
        opts = str.split(opts, ':')
        query = {
            'track': opts[0],
            'artist': opts[1],
            'limit': 1
        }
        print 'searching track: "%s" of Artist: "%s"' % (opts[0], opts[1])
    else:
        query = {
            'track': opts,
            'limit': 1
        }
        print 'searching track: "%s"' % (opts)

    params= setParams(query)
    request= URL_BASE + urllib.urlencode(params)
    print 'url search:', request
    try:
        response = urllib2.urlopen(request)
        handleRequest(response)
    except urllib2.HTTPError as e:
        print 'Error:', e.code, 'the url:', e.url, e.reason
    except urllib2.URLError as e:
        print 'Error with the url:', e.reason

def processM3u(arg):
    print "processM3u:", arg

def processPls(arg):
    print "processPls:", arg

def processXspf(arg):
    print "processXspf:", arg

def loadPLaylist(fich):
    if os.path.isfile(fich):
        try:
            ext = os.path.splitext(fich)[1][1:].lower()
            if ext == 'm3u':
                processM3u(fich)
            elif ext == 'pls':
                processPls(fich)
            elif ext == 'xspf':
                processXspf(fich)
            else:
                print "this file type is not supported"
        except Exception as e:
            print "An error occurred while processing the file:", fich
            print "Error:", e
    else:
        print "The file: %s does not exist, check the path or filename" % (fich)

#arguments list
parser = argparse.ArgumentParser()
parser.add_argument("-s", '--search', help="search by song or artist", type=search)
parser.add_argument("-l", '--load', help="load a playlist", type=loadPLaylist)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

if __name__ == '__main__':
    args = parser.parse_args()
