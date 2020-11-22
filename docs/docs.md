# This is the documentation to media downloader
First things first, if you wish to know more about use cases. Refer to [example.py](https://www.github.com/YJH16120/media-downloader/example.py).
For any of you that would like a detailed explanation of how the code works, you can referen to the same file [example.py](https://www.github.com/YJH16120/media-downloader/example.py).
Although this usually isn't needed for the everyday user. You can read it if you want, but it's mostly for contributors. If not just ignore the section, you can tell because there is a massive chunk of text.

The preferred way to import either `Unsplash` or `Media` and other packages that follows:
```
# For Unsplash
import image.main()

# For Media
import video.main()
```

# Part 1: Unsplash (Image downloader)
### image.Unsplash(self, term, quality="small")
`self` the object itself

`term` accepts a string; The image of what you want to download.

`quality` accepts a string, dictates the download quality of the image. Accepted values: `raw`, `full`, `regular`, `small`, `thumb`. These are in descending order of quality.

__Important note:__ the `main()` function servers as an entry point to interact with the classes, and has no effect on the code. Other than being responsible for starting the download process which includes: 1. Querying the user for what to download. 2. Sending HTTP requests. 3. Downloading the files.
In order to change the functionality you must change the classes and **not** the contents of `main()`

### image.Unsplash.download(self)
`self` the object itself
When calling this class method, a new folder called "contents" will be made, automatically if it doesn't exist. If it does then it will proceed, as normal.

# Part 2: Media (The video downloader)
### video.Media(self, video, mp3=False)
`self` the object itself

`term` accepts a string; The link or title of the video.

`mp3` accepts a boolean, i.e. True/False.

### video.Media.GetLink(self):
`self` the object itself

### video.Media.exists(self):
`self` the object itself
This method functions exactly like `video.Unslpash.download()`, only difference is it won't download the file immediately. It just checks if a folder called 'media' exists. If it does, it will proceed with the download, if not, it will make one then proceed with the download.

### video.Media.download(self):
`self` the object itself
A quick note: this method calls upon, `GetLink()` method, as well as, `exists()` method.

__Important note:__ the `main()` function servers as an entry point to interact with the classes, and has no effect on the code. Other than being responsible for starting the download process which includes: 1. Querying the user for what to download. 2. Sending HTTP requests. 3. Downloading the files.
In order to change the functionality you must change the classes and **not** the contents of `main()`