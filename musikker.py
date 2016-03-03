#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse, sys, os, urllib2, json

from collections import namedtuple

URL_BASE = 'https://api.spotify.com/v1/search?q='

if sys.platform.startswith('linux'):
    os.system('clear')
elif sys.platform.startswith('win'):
    os.system('cls')

request = urllib2.Request(URL_BASE+'track:lacrymosa%20artist:evanescence&type=track&limit=1')
opener = urllib2.build_opener()
stream = opener.open(request)
print 'getting json data...', stream.read()
