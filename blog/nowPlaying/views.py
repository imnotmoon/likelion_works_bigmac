from django.shortcuts import render

# Create your views here.
def nowPlaying(request):
    return render(request, 'nowplaying.html')