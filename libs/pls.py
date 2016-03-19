import log, os
import ConfigParser

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # for python ver. < 3.0

def getPlaylist(config, section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            track = config.get(section, option)
            if option != 'numberofentries':
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    log.err("skip: %s" % option)
        except:
            log.err("exception on %s!" % option)
            dict1[option] = None
    return dict1

def proccess (args):
    log.warn("preparing the m3u playlist:", args)
    config = ConfigParser()
    config.read(args)
    playlists = getPlaylist(config, "playlist")
    return playlists
