from base import *
from time import sleep
import os, sys

from pytube import YouTube
from bs4 import BeautifulSoup as BS

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Media(Link):
    def __init__(self, video, mp3=False):
        super().__init__(video)
        self.url = f"https://www.youtube.com/results?search_query={self.term}"
        self.link = False
        self.mp3 = mp3

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

def main():
    video = input("Title of video you want to download: ")
    M = Media(video)
    M.download()

if __name__ == "__main__":
    main()