#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse, os, urllib2, json, urllib
from collections import namedtuple
from libs import m3u, pls, log

URL_BASE = 'https://api.spotify.com/v1/search?'


def handleRequest(stream):
    req = stream.read()
    # the magic!
    obj = json.loads(req, object_hook=lambda d: namedtuple('musikker', d.keys())(*d.values()))

    log.success('Done!')
    log.info('Artist:', obj.tracks.items[0].artists[0].name)
    log.info('Album:', obj.tracks.items[0].album.name)
    log.info('Track:', obj.tracks.items[0].name)
    log.info('Spotify uri:', obj.tracks.items[0].uri)

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

def search(opts):
    query= {}
    if ':' in opts:
        opts = str.split(opts, ':')
        query = {
            'track': opts[0],
            'artist': opts[1],
            'limit': 1
        }
        log.success('searching track: "%s" of Artist: "%s"' % (opts[0], opts[1]))
    else:
        query = {
            'track': opts,
            'limit': 1
        }
        log.success('searching track: "%s"' % (opts))

    params= setParams(query)
    request= URL_BASE + urllib.urlencode(params)
    log.info('url to search:', request)
    try:
        response = urllib2.urlopen(request)
        handleRequest(response)
    except urllib2.HTTPError as e:
        log.err('Error:', e.code, 'the url:', e.url, e.reason)
    except urllib2.URLError as e:
        log.err('Error with the url:', e.reason)

def loadPLaylist(fich):
    if os.path.isfile(fich):
        try:
            ext = os.path.splitext(fich)[1][1:].lower()
            if ext == 'm3u':
                m3u.proccess(fich)
            elif ext == 'pls':
                pls.proccess(fich)
            elif ext == 'xspf':
                log.warn("xspf not supported yet")
            else:
                log.err("this file type is not supported")
        except Exception as e:
            log.err("An error occurred while processing the file:", fich)
            log.err("Error:", e)
    else:
        log.err("The file: %s does not exist, check the path or filename" % (fich))

#arguments list
parser = argparse.ArgumentParser()
parser.add_argument("-s", '--search', help="search by song or artist", type=search)
parser.add_argument("-l", '--load', help="load a playlist", type=loadPLaylist)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')

if __name__ == '__main__':
    log.clear()
    args = parser.parse_args()
