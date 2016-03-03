# Musikker
**Export your local playlists to Spotify, using the Web API and Python**

## Requeriments
- [python](http://wxpython.org/download.php)  2.7.x


## How to use
Clone this repo.

    git clone https://github.com/diniremix/musikker.git


```python
python musikker.py playlist.m3u
```

## Parameters
> **[-v, --v, --version]** print the current version
> **[-s, --s, --search]** search by song or artist
> **[-l, --l, --load]** load a playlist (m3u, pls, xspf)

## Examples
- search by song and artist:

```python
python musikker.py -s 'lithium:nirvana'
```

> Note the **":"** character separator

- song search (only)

```python
python musikker.py -s 'Over the Rainbow'
```

- load a playlist
```python
python musikker.py -l awesomeMix.m3u
```

> will support playlist's M3U, PLS and xspf

## ToDO
- fix the limit (default 1)
- Import from m3u playlist
- Import from pls playlist
- Import from xspf playlist

## Thanks to
- [Frankity](https://github.com/Frankity/)
- [jda](https://github.com/jacadenac)
- [Stack Overflow forum](http://goo.gl/4t0twE)

## License

The full text of the license can be found in the file LGPL.txt

### Contact
[Diniremix](https://github.com/diniremix)

email: *diniremix [at] gmail [dot] com*
