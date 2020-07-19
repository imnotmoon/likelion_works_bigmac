import urllib.request
import os
import sys
from bs4 import BeautifulSoup

def movieList():
    api = 'http://175.125.91.94/oasis/service/rest/meta16/getkobis01'

    request = urllib.request.Request(api)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode==200:
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code : " + str(rescode))
        return str(500)

def movieInfo():
    f = open('moviePage.html', mode='wt', encoding='utf-8')
    result = []
    with urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn') as response:
        html = response.read().decode('utf-8')
        soup_each = BeautifulSoup(html, 'lxml')
        for div in soup_each.find_all("div", class_="thumb"):
            img = (div.find('a').find('img').get('alt'), div.find('a').find('img').get('src'))
            result.append(img)
        # f.write(html)
    return result[:15]

movieInfo()