# Using Unsplash to download images
from media_downloader import Unsplash

# Main method
un = Unsplash("ferraris", quality="thumb")
un.download()

"""
First an Unsplash object is created, it accepts a string of your desired download.

Next it there is a space in that string, it will split it up by spaces, then join each space with a "+" sign, to construct a url.

A request is then sent to that url, and it's json data is extracted. It will then check if the file 'content' exists or not, if not it will create one, if it does it will proceed directly to the download phase.

The download phase will be different depending on what resolution of the image you want to download.

The json data will be parsed to access the list of images. Then the list will be iterated, and the id of the picture will be taken, same for the image url.

The image id will be the file name, and another request is sent to the image url and the json data will be extracted again.

with the use of a context manager a file .png file with the id as it's name will be made. And all of the bytes of the images will be written, to said file. Then a download confirmation message appear.
"""

# Using Media to downlaod youtube videos
from media_downloader import Media
M = Media("Still it feels ptx", mp3=True)
M.download()

"""
The creation, and download process is similar to the Unsplash downloader. An object is created, followed by the string of your desired download. It will split the string by spaces and join them with "+" signs if there are spaces, and a url will be constructed

A confirmation message asking if it's the video you want. If not, there will be a list to choose from, which you can reference by number. The link will then be extracted from the source code(html).

Then it will create a youtube object. Then download video to the media file. A folder called "media" will be made, if it hasn't been made already.

If mp3 is True when creating the Media object, it will rename the file and change it's extension to a .mp3 file, the name of the file will remain the same, only the file extension is changed.

If mp3 isn't True, then it will proceed to download as per normal. As an .mp4 in the "media" folder.
"""

