from django.shortcuts import render, redirect
from .models import Articles
from django.utils import timezone


# Create your views here.
def article(request):
    articles = Articles.objects.all()
    return render(request, 'article.html', {'articles' : articles})

def create(request):
    article = Articles()
    article.title = request.GET['title']
    article.body = request.GET['body']
    article.pub_date = timezone.datetime.now()
    article.save()
    return redirect('/articles/')

def write(request):
    
    return render(request, 'write.html')
