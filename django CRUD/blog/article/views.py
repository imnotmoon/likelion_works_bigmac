from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles
from django.utils import timezone
from .form import ArticleUpdate
from faker import Faker
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def article(request):
    articles = Articles.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'article.html', {'articles' : articles, 'posts' : posts})

def create(request):
    article = Articles()
    article.title = request.GET['title']
    article.body = request.GET['body']
    article.author = request.user.username
    article.pub_date = timezone.datetime.now()
    article.save()
    return redirect('/article/')

def write(request):
    print(request.user.is_authenticated)
    print(request.user.username)
    if request.user.is_authenticated :
        return render(request, 'write.html')
    else :
        return render(request, 'article.html', {'error':'Session Required'})

def detail(request, article_id):
    article_detail = get_object_or_404(Articles, pk=article_id)
    return render(request, 'detail.html', {'article' : article_detail})

def update(request, article_id):
    return render(request, 'update.html', {'article_id' : article_id})

def delete(request, article_id):
    Articles.objects.get(id=article_id).delete()
    return redirect('/article/')

def update(request, article_id):
    article = Articles.objects.get(id=article_id)
    if request.method =='POST':
        form = ArticleUpdate(request.POST)
        if form.is_valid():
            print("pass")
            article.title = form.cleaned_data['title']
            article.body = form.cleaned_data['body']
            article.pub_date=timezone.now()
            article.save()
            return redirect('/article/')
    else:
        form = ArticleUpdate(instance = article)
 
        return render(request,'update.html', {'form':form})

def fake(request):
    for i in range(10):
        blog = Articles()
        myfake = Faker('ko_KR')
        blog.title = myfake.sentence()
        blog.author = myfake.name()
        txt = ''
        for j in range(10):
            txt = txt + myfake.text()
        blog.body = txt
        blog.pub_date = timezone.datetime.now()
        blog.save()
    return redirect('/article/')
