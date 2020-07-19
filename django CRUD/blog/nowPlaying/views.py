from django.shortcuts import render
from main import conn
from main.models import Movies
import xmltodict

# Create your views here.
def nowPlaying(request):
    movieList = xmltodict.parse(conn.movieList())
    movieThumbnails = conn.movieInfo()
    items = []
    for movie in movieList['response']['body']['items']['item'] :
        m = Movies()
        m.title = movie['title']
        for thumbnails in movieThumbnails:
            if m.title in thumbnails[0]:
                print(thumbnails)
                m.poster = thumbnails[1]
        m.grade = int(movie['grade'][4:6])
        m.subDescription = movie['subDescription']
        m.postdate = movie['issuedDate']
        items.append(m)
    return render(request, 'nowplaying.html', {'movielist' : items})