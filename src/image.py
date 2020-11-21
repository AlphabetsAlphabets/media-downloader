import requests, json, aiohttp, requests, asyncio
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

    def __init__(self, term, quality="small"):
        super().__init__(term)
        if quality in self.resos:
            self.quality = quality
        else:
            self.quality = "small"

        self.url = f"https://unsplash.com/napi/search?query={self.term}&xp=&per_page=20"

    def harvest_link(self):
        r = requests.get(self.url, headers=self.creds).json()
        total = r['photos']['results']
        images = [x['urls'][self.quality] for x in total]

        return images

    async def download(self):
        images = self.harvest_link()

        exists = os.path.exists("content")
        if not exists:
            os.mkdir("content")
            path = os.getcwd() + "\\content"
        else:
            path = os.getcwd() + "\\content"

        async with aiohttp.ClientSession() as session:
            for count, links in enumerate(images, start=1):
                async with session.get(links) as r:
                    bytes = await r.read()
                    with open(f"{path}\\image{count}.png", 'wb') as f:
                        f.write(bytes)

        sys.exit()

def main():
    term = input("Images of what you want to download: ")
    un = Unsplash(term)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(un.download())

if __name__ == "__main__":
    main()