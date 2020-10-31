import requests
from requests.auth import HTTPBasicAuth
import os, sys, shutil
import json
# something
class Unsplash:
    creds = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "en-US,en;q=0.5",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
    }

    def __init__(self, term):
        self.term = term
        self.url = f"https://unsplash.com/napi/search?query={self.term}&xp=&per_page=20"

    def download(self):
        r = requests.get(self.url, headers=self.creds).json()

        exists = os.path.exists("content")
        if not exists:
            os.mkdir("content")
            path = os.getcwd() + "\\content"
        else:
            path = os.getcwd() + "\\content"

        total = r['photos']['results']
        for item in total:
            name = item['id']
            image = item['urls']['small']

            with open(f"{path}\\{name}.jpg", 'wb') as f:
                r = requests.get(image, headers=self.creds).content
                f.write(r)

        print(f"Download complete. Downloaded a total of: {len(total)}")
        sys.exit()

    def Check_Response(self):
        r = requests.get(self.url, headers=self.creds)
        return r

class Instagram:
    def __init__(self, user):
        self.user = user

    def download(self):
        pass

