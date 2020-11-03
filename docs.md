# This is the documentation to media downloader
First things first, if you wish to know more about use cases. Refer to (example.py)[https://www.github.com/YJH16120/media-downloader/example.py]. Next, for detailed explanations of how it works. Refer to the same file.

The preferred way to import either `Unsplash` or `Media` and other packages that follows:
```
# For Unsplash
from main import Unsplash

# For Media
from main import Media
```

# Part 1: Unsplash (Image downloader)
### main.Unsplash(self, term)
`self` the object itself

`term` accepts a string; The image of what you want to download.

### main.Unsplash.download(self)
`self` the object itself
When calling this class method, a new folder called "contents" will be made, automatically if it doesn't exist. If it does then it will proceed, as normal.

# Part 2: Media (The video downloader)
### main.Media(self, video)
`self` the object itself

`term` accepts a string; The link or title of the video.

### main.Media.GetLink(self):
`self` the object itself

### main.Media.exists(self):
`self` the object itself
This method functions exactly like `main.Unslpash.download()`, only difference is it won't download the file immediately. It just checks if a folder called 'media' exists. If it does, it will proceed with the download, if not, it will make one then proceed with the download.

### main.Media.download(self):
`self` the object itself
A quick note: this method calls upon, `GetLink()` method, as well as, `exists()` method.

