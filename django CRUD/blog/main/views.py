from django.shortcuts import render
from .models import Movies
from main import conn
import xmltodict
from collections import OrderedDict

# Create your views here.
def home(request):
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
        
    return render(request, 'main.html', {'movielist' : items})

def donate(request):
    return render(request, 'donate.html')

def mylocation(request):
    f = open('main/key', 'r')
    key = f.readline()
    print(key)
    return render(request, 'mylocation.html', {'key' : key})