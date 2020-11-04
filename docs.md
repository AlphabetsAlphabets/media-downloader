# This is the documentation to media downloader
First things first, if you wish to know more about use cases. Refer to [example.py](https://www.github.com/YJH16120/media-downloader/example.py).
For any of you that would like a detailed explanation of how the code works, you can referen to the same file [example.py](https://www.github.com/YJH16120/media-downloader/example.py).
Although this usually isn't needed for the everyday user. You can read it if you want, but it's mostly for contributors. If not just ignore the section, you can tell because there is a massive chunk of text.

The preferred way to import either `Unsplash` or `Media` and other packages that follows:
```
# For Unsplash
from media_downloader import Unsplash

# For Media
from media_downloader import Media
```

# Part 1: Unsplash (Image downloader)
### media_downloader.Unsplash(self, term, quality)
`self` the object itself

`term` accepts a string; The image of what you want to download.

`quality` accepts a string, dictates the download quality of the image. Accepted values: `raw`, `full`, `regular`, `small`, `thumb`. These are in descending order of quality.

### media_downloader.Unsplash.download(self)
`self` the object itself
When calling this class method, a new folder called "contents" will be made, automatically if it doesn't exist. If it does then it will proceed, as normal.

# Part 2: Media (The video downloader)
### media_downloader.Media(self, video, mp3=False)
`self` the object itself

`term` accepts a string; The link or title of the video.

`mp3` accepts a boolean, i.e. True/False.

### media_downloader.Media.GetLink(self):
`self` the object itself

### media_downloader.Media.exists(self):
`self` the object itself
This method functions exactly like `media_downloader.Unslpash.download()`, only difference is it won't download the file immediately. It just checks if a folder called 'media' exists. If it does, it will proceed with the download, if not, it will make one then proceed with the download.

### media_downloader.Media.download(self):
`self` the object itself
A quick note: this method calls upon, `GetLink()` method, as well as, `exists()` method.

