'''
@ 하나의 계정에서 모든 썸네일 가져오기
2021.12.15. 최종수정
'''

from bin.utils import download_img, fb_login,thumb_urls, lazy

def oneacc_all_thumbs_download(driver,url,id=None,pw=None):
    SCROLL_TIME=3
    all_urls=[]
    fb_login(driver,url,id,pw)
    lazy(1)
    last_height = driver.execute_script("return document.body.scrollHeight")
    moreBTN=driver.find_elements_by_css_selector("#react-root > div > div > section > main > div > div._2z6nI > div.qF0y9.Igw0E.rBNOH.eGOV_._4EzTm > div > button > div")
    if(moreBTN):
        moreBTN[0].click()
    while(True):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        lazy(SCROLL_TIME)
        new_height=driver.execute_script("return document.body.scrollHeight")
        if(new_height==last_height and all_urls!=[]):
            break
        last_height=new_height
        lazy(1)
        all_urls=thumb_urls(driver,'all_thumbs',all_urls)
    for url in all_urls:
        download_img(url)