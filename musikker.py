#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse, sys, os, urllib2, json

URL_BASE = 'https://api.spotify.com/v1/search?q='

if sys.platform.startswith('linux'):
    os.system('clear')
elif sys.platform.startswith('win'):
    os.system('cls')

request = urllib2.Request(URL_BASE+'track:lacrymosa%20artist:evanescence&type=track&limit=1')
opener = urllib2.build_opener()
print 'getting json data...'

try:
    stream = opener.open(request)
    print stream.read()
except urllib2.HTTPError as e:
    print 'Error:', e.code, 'the url:', e.url, e.reason
except urllib2.URLError as e:
    print 'Error with the url:', e.reason
