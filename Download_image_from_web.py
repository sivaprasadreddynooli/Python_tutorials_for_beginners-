import random
import urllib.request

def download_image_from_web(url):
    number = random.randrange(1,1000)
    filename= str(number) + '.jpg'
    urllib.request.urlretrieve(url,filename)

download_image_from_web("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbVZdZYYgszI1_zicNH_yfzR9CWUbh66Sbby4eJQDkwP8APlFv")