from flask import Blueprint, render_template,request
from urllib.request import urlopen
from urllib.parse import quote
import json

data = Blueprint('data', __name__)

URL_ARTIST = "https://api.deezer.com/artist/{0}/"
URL_ALBUM = "https://api.deezer.com/album/{0}/"

@data.route('/artist/<int:id>')
def artists(id):
    artist = getArtist(id)
    artistTop,getTop = getArtistTop(id)
    artistAlbum = getArtistAlbum(id)
    return render_template('artist.html',tops = artistTop,getTop=getTop,artist = artist ,albums = artistAlbum)

@data.route('/album/<int:id>')
def albums(id):
    tracks = getAlbumsTracks(id)
    albums = getAlbums(id)
    return render_template('album.html',tracks = tracks, albums = albums )

def getArtist(id):
    url = URL_ARTIST.format(id)
    data = urlopen(url).read()
    parsed = json.loads(data)
    return parsed


def getArtistTop(id):
    url = URL_ARTIST.format(id) 
    urlTop = url + "top"
    dataTop = urlopen(urlTop).read()
    parsedTop = json.loads(dataTop)
    topArr = []
    top = {} 
    if parsedTop['total'] == 0:
        nums = 0
        top['total'] = 0
    elif parsedTop['total'] < 5:
        nums = parsedTop['total']
        top['total'] = parsedTop['total']
    else:
        nums = 4
        top['total'] = 4
    for n in range(0,nums):
        title = parsedTop['data'][n]['title']
        link = parsedTop['data'][n]['link'] 
        preview = parsedTop['data'][n]['preview'] 
        artistId = parsedTop['data'][n]['artist']['id']
        artist = parsedTop['data'][n]['artist']['name']
        cover = parsedTop['data'][n]['album']['cover']
        album = parsedTop['data'][n]['album']['title']
        albumId = parsedTop['data'][n]['album']['id']
        tops = {'title':title,
                'link':link,
                'preview':preview ,
                'artistId':artistId,
                'artist':artist,
                'cover':cover,
                'album':album,
                'albumId':albumId,
                }
        topArr.append(tops)
    return topArr,top

def getArtistAlbum(id):
    url = URL_ARTIST.format(id) 
    urlAlbum = url + "albums"
    dataAlbum = urlopen(urlAlbum).read()
    parsedAlbum = json.loads(dataAlbum)
    albumArr = []
    for n in parsedAlbum['data']:
        alId = n['id']
        title = n['title']
        cover =  n['cover_medium']
        fans = n['fans']
        release_date = n['release_date']
        albums = {'alId': alId,
                'title': title,
                'cover': cover,
                'fans':fans,
                'release_date':release_date
                }
        albumArr.append(albums)
    return albumArr

def getAlbums(id):
    url = URL_ALBUM.format(id) 
    data= urlopen(url).read()
    parsed= json.loads(data)
    return parsed

def getAlbumsTracks(id):
    url = URL_ALBUM.format(id) 
    urlTracks = url + "tracks"
    dataTracks = urlopen(urlTracks).read()
    parsedTracks = json.loads(dataTracks)
    tracksArr = []
   
    for n in parsedTracks['data']:
        title = n['title']
        link = n['link'] 
        preview = n['preview'] 
        artistId = n['artist']['id']
        artist = n['artist']['name']
        tracks = {
                'title':title,
                'link':link,
                'preview':preview ,
                'artistId':artistId,
                'artist':artist
                }
        tracksArr.append(tracks)
    return tracksArr





    

    

