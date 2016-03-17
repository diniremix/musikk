import log, os
from tinytag import TinyTag
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
            track=config.get(section, option)
            if option != 'numberofentries':
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
                    print "skip: %s" % option
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def checkFile (name):
    if os.path.isfile(name):
        try:
            tag = TinyTag.get(name)
            log.warn('tag info:')
            log.info('Artist:', tag.artist)
            log.info('Album:', tag.album)
            log.info('Title:', tag.title)
            log.info('Track:',tag.track)
            try:
                import musikker
                song=str(tag.title+':'+tag.artist)
                print 'song:', song
                musikker.search(song)
            except Exception as e:
                log.err("An error occurred while getting spotify info:", str(e))
        except Exception as e:
            log.err("An error occurred while getting metadata of the file:", name)
            log.err("Error:", e)
    else:
        log.err("The file: %s does not exist, check the path or filename" % (name))

def proccess (args):
    log.warn("preparing the m3u playlist:", args)
    config = ConfigParser()
    config.read(args)
    sections = config.sections()
    playlists = getPlaylist(config, "playlist")
    for name in playlists:
        print 'el:', playlists[name]
        checkFile(playlists[name])

    """
    log.warn("searching playlist section:", sections)
    log.info("sections found:")
    log.success('', sections)
    log.info("Options found:")
    options = config.options(sections[0])
    log.success('', options)
    log.info("Number Of Entries:")
    options = config.options(sections[0])
    entries = config.get(sections[0], options[0])
    log.success('', entries)
    log.info("Track found:")
    entries1 = config.get(sections[0], options[1])
    log.success('', entries1)
    checkFile(entries1)
    """

def getData(args):
    tag = TinyTag.get('/some/music.mp3')
    print('This track is by %s.' % tag.artist)
    print('It is %f seconds long.' % tag.duration)
    log.warn("preparing the m3u playlist:", args)
