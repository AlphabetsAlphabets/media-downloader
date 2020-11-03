# Using Unsplash to download images
from media_downloader import Unsplash

# Main method
un = Unsplash("ferraris")
un.download()

# Alternative method
term = input("Image to download: ")
un = Unsplash(term)
un.download()

"""
First an Unsplash object is created, it accepts a string of your desired download.

Next it there is a space in that string, it will split it up by spaces, then join each space with a "+" sign, to construct a url.

A request is then sent to that url, and it's json data is extracted. It will then check if the file 'content' exists or not, if not it will create one, if it does it will proceed directly to the download phase.

The json data will be parsed to access the list of images. Then the list will be iterated, and the id of the picture will be taken, same for the image url.

The image id will be the file name, and another request is sent to the image url and the json data will be extracted again.

with the use of a context manager a file .png file with the id as it's name will be made. And all of the bytes of the images will be written, to said file. Then a download confirmation message appear.
"""

# Using Media to downlaod youtube videos
