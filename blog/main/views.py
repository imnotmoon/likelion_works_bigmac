from django.shortcuts import render
from .models import Movies
from main import conn
import xmltodict
from collections import OrderedDict

# Create your views here.
def home(request):
    movieList = xmltodict.parse(conn.movieList())
    items = []
    for movie in movieList['response']['body']['items']['item'] :
        print("title : " + movie['title'])
        print("  grade : " + movie['grade'])
        print("  subDescription : " + movie['subDescription'])
        # print("  issuedDate : " + movie['issuedDate'])
        movie = Movie()
        movie.title = movie['title']
        movie.

    return render(request, 'main.html', {'movielist' : movieList})