from flask import Blueprint, render_template,request
from urllib.request import urlopen
from urllib.parse import quote
import json

chart = Blueprint('chart', __name__)

@chart.route('/charts')
def charts():
    cTrack = chTrack()
    cArtist = chArtist()
    cAlbum = chAlbum()
    return render_template('charts.html',tracks = cTrack, artists = cArtist, albums = cAlbum)

def chTrack():
    url = "https://api.deezer.com/chart/0/tracks"
    data = urlopen(url).read()
    parsed = json.loads(data)
    chartArr = []
    if parsed.get('data'):
        nums = parsed['total']
        for n in range(0,nums):
            track = parsed['data'][n] 
            title = track['title']
            link = track['link']
            position = track['position']
            preview = track['preview']
            arName = track['artist']['name']
            arId = track['artist']['id']
            arPic = track['artist']['picture_big']
            arLink = track['artist']['link']
            alTitle = track['album']['title']
            alCover = track['album']['cover_big']
            alId = track['album']['id']
            chart ={'title':title,  
                    'link':link ,
                    'position':position ,
                    'preview':preview ,
                    'name':arName ,
                    'arId':arId,
                    'arPic':arPic ,
                    'arLink':arLink,
                    'album':alTitle,
                    'cover':alCover,
                    'alId':alId
                    } 
            chartArr.append(chart)
        return chartArr

def chArtist():
    url = "https://api.deezer.com/chart/0/artists"
    data = urlopen(url).read()
    parsed = json.loads(data)
    urlArtist = "https://api.deezer.com/artist/{0}"
    chartArr = []
    if parsed.get('data'):
        nums = parsed['total']
        for n in range(0,nums):
            artist = parsed['data'][n] 
            urlArtists =  urlArtist.format(artist['id'])
            data2 = urlopen(urlArtists).read()
            parsed2 = json.loads(data2)
            artist['fans'] = parsed2['nb_fan']
            chartArr.append(artist)
        return chartArr

def chAlbum():
    url = "https://api.deezer.com/chart/0/albums"
    data = urlopen(url).read()
    parsed = json.loads(data)
    chartArr = []
    if parsed.get('data'):
        nums = parsed['total']
        for n in range(0,nums):
            album = parsed['data'][n] 
            title = album['title']
            link = album['link']
            position = album['position']
            arName = album['artist']['name']
            alId = album['id']
            arId = album['artist']['id']
            cover  = album['cover_big']
            charts ={'title':title,  
                    'link':link ,
                    'position':position ,
                    'name':arName ,
                    'arId':arId,
                    'alId':alId ,
                    'cover':cover
                    } 
            chartArr.append(charts)
        return chartArr
