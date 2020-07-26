from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from faker import Faker

def addFakeMembers(request) :
    for i in range(3):
        myfake = Faker('ko_KR')
        user = User.objects.create_user(
            myfake.name(), password=myfake.ean(length=8)
        )
    
    return render(request, 'signup.html', {'alert':'Fake members generated'})

def signup(request):
    # 1. 비밀번호와 비밀번호 확인이 일치하는지?
    # 2. 이미 등록된 아이디가 아닌지?
    if request.method == 'POST' :
        if request.POST['password'] != request.POST['passwordCheck']:
            return render(request, 'signup.html', {'error':"Password should match"})
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'signup.html', {'error' : "Username has already been taken"})
        except:
            user = User.objects.create_user(
                request.POST['username'], password = request.POST['password']
            )
            auth.login(request, user)
            return redirect('/')
    else :
        return render(request, 'signup.html')

def login(request) :
    if request.method =='POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request, 'login.html', {'error' : 'Invalid Username or Password'})
    else :
        return render(request, 'login.html')

def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('/')
    else :
        return render(request, 'signup.html')