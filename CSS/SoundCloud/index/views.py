from django.shortcuts import render
from faker import Faker

# Create your views here.
def index(request) :
    faker = Faker()
    return render(request, 'index.html')