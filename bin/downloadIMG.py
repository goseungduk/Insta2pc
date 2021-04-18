'''
@ 게시물에서 사진따오기
2021.04.18. 최종수정
'''

import urllib.request as urlREQ
import random, string
# downloading pics with src
def download_img(url):
    tmp=''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
    urlREQ.urlretrieve(url,"test"+tmp+".jpg")