from flask import Blueprint, render_template,request,flash
from urllib.request import urlopen
from urllib.parse import quote
import json
search = Blueprint('search', __name__)

URL_ARTIST="https://api.deezer.com/search/artist?q={0}"
URL_ALBUM="https://api.deezer.com/search/album?q={0}"
URL_TRACK = "https://api.deezer.com/search/track?q={0}"


@search.route('/search',methods = ['GET','POST'])
def searchs():
    if request.method == 'POST':
        if not request.form['search']:
            flash('Please enter the fields', 'error')
        else:
            names = request.form.get('search')
            name = quote(names)
            artists = searchArtist(name)
            tracks = searchTrack(name)
            albums = searchAlbum(name)
            return render_template('search.html',artists=artists,tracks = tracks,albums=albums)
    return render_template('search.html')

def searchArtist(name):
    url = URL_ARTIST.format(name)
    data = urlopen(url).read()
    parsed = json.loads(data)
    artists = []
    if parsed['total'] != 0:
        for n in parsed['data']:
            artists.append(n)
    else:
        tracks = None
    return artists

def searchTrack(name):
    url = URL_TRACK.format(name)
    data = urlopen(url).read()
    parsed = json.loads(data)
    tracks = []
    if parsed['total'] != 0:
        for n in parsed['data']:
            tracks.append(n)
    else:
        tracks = None
    return tracks

def searchArtist(name):
    url = URL_ARTIST.format(name)
    data = urlopen(url).read()
    parsed = json.loads(data)
    artists = []
    if parsed['total'] != 0:
        for n in parsed['data']:
            artists.append(n)
    else:
        tracks = None
    return artists

def searchAlbum(name):
    query = quote(name)
    url = URL_ALBUM.format(name)
    data = urlopen(url).read()
    parsed = json.loads(data)
    albums = []
    if parsed['total'] != 0:
        for n in parsed['data']:
            albums.append(n)
    else:
        albums = None
    return albums

