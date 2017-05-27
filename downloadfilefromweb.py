import random
import urllib.request

def download_from_web(url):
    name = random.randrange(1,1000)
    fullname = str(name) + '.jpg'
    urllib.request.urlretrieve(url,fullname)


download_from_web('http://www.thehindu.com/multimedia/dynamic/03072/THJVN_DELHI_SMOG_3072371f.jpg')