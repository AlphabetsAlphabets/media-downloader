import requests
import json
import os, sys, shutil
from time import sleep

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Unsplash:
    creds = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "en-US,en;q=0.5",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
    }

    def __init__(self, term):
        if " " in term:
            term = term.split(" ")
            self.term = "+".join(term)
        else:
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

class Youtube:
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)

    def __init__(self, term):
        if " " in term:
            term = term.split(" ")
            self.term = "+".join(term)
        else:
            self.term = term

        self.url = f"https://unsplash.com/napi/search?query={self.term}&xp=&per_page=20"

    def GetLink(self):
        self.driver.get(self.url)
        sleep(0.5)
        source = self.driver.execute_script("return document.documentElement.outerHTML")
        self.driver.quit()
        soup = BS(source, "lxml")

        videoClass = "style-scope ytd-vertical-list-renderer"
        videos = soup.find_all("div", class_=videoClass)
        for index, video in enumerate(videos, start=1):
            vidLink = video.ytd-video-renderer.div.ytd-thumbnail.a
            print(f"{index}. {vidLink}")

        sys.exit()

    def download(self):
        pass
