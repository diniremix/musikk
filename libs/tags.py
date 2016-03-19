import log, os
from tinytag import TinyTag

def getInfo (name):
    if os.path.isfile(name):
        try:
            tag = TinyTag.get(name)
            log.warn('tag info:')
            log.info('Artist:', tag.artist)
            log.info('Album:', tag.album)
            log.info('Title:', tag.title)
            log.info('Track number:', tag.track)

        except Exception as e:
            log.err("An error occurred while getting metadata of the file:", name)
            log.err("Error:", e)
    else:
        log.err("The file: %s does not exist, check the path or filename" % (name))

def getMetaData(playlists):
    log.info('accessing metadata...')
    for track in playlists:
        getInfo(playlists[track])
