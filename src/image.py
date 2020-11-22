import requests, json, aiohttp, requests, asyncio, random, time
import os, sys

from base import *

class Unsplash(Link):
    creds = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "en-US,en;q=0.5",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
    }

    resos = ['raw', 'full', 'regular', 'small', 'thumb']
    file = 0
    def __init__(self, term, quality="small"):
        super().__init__(term)
        if quality in self.resos:
            self.quality = quality
        else:
            self.quality = "small"

        self.url = f"https://unsplash.com/napi/search?query={self.term}&xp=&per_page=50"

    def harvest_link(self):
        r = requests.get(self.url, headers=self.creds).json()
        total = r['photos']['results']
        self.totalImages = len(total)
        self.link = [x['urls'][self.quality] for x in total]

        return self.link

    async def queue(self, link):
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as r:
                bytes = await r.read()
                with open(f"{self.path}\\{self.term}_{self.file}.png", 'wb') as f:
                    f.write(bytes)
                    self.file += 1

    async def path_creation(self):
        exists = os.path.exists("content")
        if not exists:
            os.mkdir("content")
            self.path = os.getcwd() + "\\content"
        else:
            self.path = os.getcwd() + "\\content"

        links = [self.queue(link) for link in self.harvest_link()]
        await asyncio.wait(links)

def main():
    term = input("Images of what you want to download: ")
    un = Unsplash(term)
    loop = asyncio.get_event_loop()

    currentTime = time.time()
    loop.run_until_complete(un.path_creation())
    finishTime = time.time() - currentTime

    print(F"Task completed in: {finishTime} seconds")
    print(f"Downloaded a total of: {un.totalImages} images")

if __name__ == "__main__":
    main()