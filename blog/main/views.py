from django.shortcuts import render
from article.models import Articles

# Create your views here.
def home(request):
    return render(request, 'main.html')