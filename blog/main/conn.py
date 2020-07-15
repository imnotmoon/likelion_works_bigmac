import urllib.request
import os
import sys

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