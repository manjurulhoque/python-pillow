import random
import urllib.request

def download_from_web(url):

    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_from_web("https://i.ytimg.com/vi/mfNcavKCVAc/maxresdefault.jpg")
