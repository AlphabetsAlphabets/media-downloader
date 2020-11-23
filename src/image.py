import aiohttp, asyncio, random, time, aiofiles
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

        self.url = f"https://unsplash.com/napi/search?query={self.term}&xp=&per_page=50"

    async def harvest_link(self, url):
        async with aiohttp.ClientSession() as s:
            async with s.get(url) as r:
                content = await r.json()
                images = content['photos']['results']
                self.totalImages = len(images)
                imageURLs = [posts['urls']["thumb"] for posts in images]
                names = [posts["id"] for posts in images]
                return names, imageURLs

    async def path_creation(self):
        exists = os.path.exists("images")
        if not exists:
            os.mkdir("images")
            path = os.getcwd() + f"\\images"
            return path

        else:
            path = os.getcwd() + f"\\images"
            return path

    async def queue(self, name, URL):
        path = await self.path_creation()
        async with aiohttp.ClientSession() as s:
            async with s.get(URL) as r:
                async with aiofiles.open(f"{path}\\{name}.png", "wb") as f:
                    await f.write(await r.read())

    async def download(self):
        imageInformation = await self.harvest_link(self.url)
        imageNames, imageLinks = imageInformation
        links = [self.queue(name, url) for name, url in zip(imageNames, imageLinks)]
        await asyncio.wait(links)

def main():
    term = input("Images of what you want to download: ")
    un = Unsplash(term)
    loop = asyncio.get_event_loop()

    currentTime = time.time()
    loop.run_until_complete(un.download())
    finishTime = time.time() - currentTime

    print(F"Task completed in: {finishTime} seconds")
    print(f"Downloaded a total of: {un.totalImages} images")

if __name__ == "__main__":
    main()