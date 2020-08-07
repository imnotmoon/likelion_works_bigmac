from django.shortcuts import render
from .models import Playlist
from faker import Faker

# Create your views here.
def index(request) :
    Playlist.objects.all().delete()
    l = [1, 2, 3, 4, 5]
    for i in l:
        for j in range(8):
            myfake = Faker('ko_KR')
            pl = Playlist()
            pl.title = myfake.word()
            pl.name = myfake.name()
            pl.img = "#"
            pl.mood = i
            pl.save()

    chill = {
        'category' : 'Chill',
        'contents': Playlist.objects.filter(mood=1)
    }
    party = {
        'category': 'Party',
        'contents': Playlist.objects.filter(mood=2)
    }
    relax = {
        'category' : 'Relax',
        'contents' : Playlist.objects.filter(mood=3)
    }
    study = {
        'category': 'Study',
        'contents': Playlist.objects.filter(mood=4)
    }
    workout = {
        'category' : 'Workout',
        'contents': Playlist.objects.filter(mood=5)
    }
    
    return render(request, 'index.html', {'playlists' : [chill, party, relax, study, workout]})