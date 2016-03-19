import log, os
from tinytag import TinyTag

def saveMetaData (fullname, data, count):
    log.warn('saving metadata of %s...' % fullname)
    filename=fullname
    thefile = open(filename, 'w')

    thefile.write("[musikker]\n")
    thefile.write("entries=%s\n" % str(count))

    for item in data:
        thefile.write("tag=%s\n" % item)
    pass
    log.success('metadata saved in:', filename)

def getMetaData(fullname, playlists):
    log.info('accessing metadata...')
    index = 0
    tagInfo = []
    for track in playlists:
        name= playlists[track]
        if os.path.isfile(name):
            try:
                filename = os.path.basename(name)
                log.success('-------------------------')
                tag = TinyTag.get(name)
                if tag.title != '' or tag.artist != '':
                    song = str(tag.title+':'+tag.artist)
                    tagInfo.append(song)
                    log.warn('tag info:', filename.encode("ascii", "ignore"))
                    log.info('Artist:', tag.artist)
                    log.info('Album:', tag.album)
                    log.info('Title:', tag.title.encode("ascii", "ignore"))
                    log.info('Track number:', tag.track)
                    index += 1
                else:
                    log.warn('WARN: no id3 info provide')

            except Exception as e:
                log.err("An error occurred while getting metadata of the file:", name)
                log.err("Error:", e)
        else:
            log.err("The file: %s does not exist, check the path or filename" % (name))
    print
    log.err('track processing:', str(index))
    saveMetaData(fullname, tagInfo, index)
