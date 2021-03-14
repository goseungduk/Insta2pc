import requests
import urllib.request as urlREQ

def download_img(url):
    urlREQ.urlretrieve(url,"test.jpg")


download_img("https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/c0.134.1080.1080a/s640x640/159871148_1339695679743363_758128885688490935_n.jpg?tp=1&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=_xOacxPmthYAX_ueQNG&oh=e237b81c18c1bb65672711c02ea84a4a&oe=60759267")

# version 1.0.0
# 1. one post, multi pics downloading
# 2. multi post, one pic downloading
