# Image-downloader & how it works
This is a simple image downloader I made. It uses the requests package, as well as os, and sys. This is to manage file operations, and to if the the file
"content" exists. If it does then, nothing happens. It just grabs the path, if not it will create a content folder, then gets it path.

Next is sends a requests to the API that Unsplash uses. Followed by converting that request to JSON data, then accessing the data such as the file name,
the image url which will be used to download the file.

A request is then sent to the image url, then all the bytes will be downloaded and written to a new `.png` file. The program will only download a maximum
of 20 images, the limit is not mutable.
