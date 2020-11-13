import requests, json
from pytube import YouTube
import os, sys, multiprocessing

from time import sleep

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Link:
    def __init__(self, term):
        if " " in term:
            term = term.split(" ")
            self.term = "+".join(term)
        else:
            self.term = term

class Unsplash(Link):
    creds = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "en-US,en;q=0.5",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
    }

    resos = ['raw', 'full', 'regular', 'small', 'thumb']

    def __init__(self, term, quality="small"):
        super().__init__(term)
        if quality in self.resos:
            self.quality = quality
        else:
            self.quality = "small"

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
            image = item['urls'][self.quality]

            with open(f"{path}\\{name}.jpg", 'wb') as f:
                r = requests.get(image, headers=self.creds).content
                f.write(r)

        sys.exit()

    def Check_Response(self):
        r = requests.get(self.url, headers=self.creds)
        return r

class Media(Link):
    def __init__(self, video, mp3=False):
        super().__init__(video)
        self.url = f"https://www.youtube.com/results?search_query={self.term}"
        self.link = False
        self.mp3 = mp3
        p = multiprocessing.Process(target=self.StartUp())
        p.start()

    def StartUp(self):
        opts = Options()
        opts.headless = True
        self.driver = webdriver.Firefox(options=opts)

    def GetLink(self):
        self.driver.get(self.url)
        sleep(1)

        source = self.driver.execute_script("return document.documentElement.outerHTML")
        self.driver.quit()
        soup = BS(source, "lxml")

        videoClass = "yt-simple-endpoint style-scope ytd-video-renderer"

        videos = soup.find_all('a', class_=videoClass)

        print(f"Is this the video you're looking for?\n{videos[0]['title']}")
        check = input("Y/n: ").lower()

        if check == "y":
            self.vidLink = videos[0]['href']
        else:
            print("Select from this selection of videos to download, and try to find yours.")
            for index, video in enumerate(videos, start=1):
               print(f"{index}. {video['title']}")

            select = int(input("Reference video by number: "))
            self.vidLink = videos[select - 1]['href']

    def exists(self):
        exists = os.path.exists("media")
        if exists == False:
            os.mkdir("media")
            self.path = os.getcwd() + "\\media"

        else:
            self.path = os.getcwd() + "\\media"

    def download(self):
        if self.link:
            yt = YT(self.url)
            stream = yt.streams[0]

            self.exists()

            file = stream.download(self.path)
            change_to = file.strip(".mp4")
            if self.mp3 == True:
                os.rename(file, f"{change_to}.mp3")

            sys.exit()
        else:
            self.GetLink()

            yt = YouTube(self.vidLink)
            stream = yt.streams[0]

            self.exists()

            file = stream.download(self.path)
            change_to = file.strip(".mp4")
            if self.mp3 == True:
                os.rename(file, f"{change_to}.mp3")

            sys.exit()
