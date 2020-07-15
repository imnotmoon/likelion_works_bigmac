from django.shortcuts import render
from .models import Articles

# Create your views here.
def article(request):
    articles = Articles.objects.all()
    return render(request, 'article.html', {'articles' : articles})