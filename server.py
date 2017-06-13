import requests
import json

def upload(filename):
    url = 'http://127.0.0.1:3000/upload'
    print 'Uploading %s' % filename
    files = {'file': open(filename, 'rb')}
    r = requests.post(url, files=files)
    print r.url, r.text

def getfilelist():
    url = 'http://127.0.0.1:3000/getfilelist'
    print 'fetching file list from server'
    return requests.get(url).json()

