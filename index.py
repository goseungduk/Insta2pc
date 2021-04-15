from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urlREQ
import time, random, string
import sys, os
from bin import oneMulti
from bin import fbLogin as FL # 임시 import 모듈 분리할 때까지만

all_thumbs=[] # 전역 변수 자제해라
def thumb_urls(driver): # 썸네일 url 따오기
    global all_thumbs
    thumbs=driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w')
    for thumb in thumbs:
        link=thumb.find_elements_by_tag_name('a')[0].get_attribute('href')
        if(link not in all_thumbs):
            all_thumbs.append(link)

def oneacc_multi_thum_download(driver,url):
    collecting_urls(driver,url)

def collecting_urls(driver,url):
    global all_thumbs
    # https://www.instagram.com/dlwlrma/
    # https://www.instagram.com/accounts/signup/
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except: # 익명으로 로그인이 무사히 되었을 때
        last_height = driver.execute_script("return document.body.scrollHeight")
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height=driver.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
            thumb_urls(driver)
    else: # 익명로그인이 잘 안되었을때
        FL.fb_login(driver,is_login_FB,url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height=driver.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
            thumb_urls(driver)
        # print(all_thumbs) 모든 게시물 가져오는 것 확인완료

def intro():
    print("<인스타그램 사진 다운로더>")
    print("1. 하나의 게시글에 있는 모든 사진 가져오기")
    print("2. 하나의 계정에 있는 모든 썸네일사진 가져오기")
    print("3. 하나의 계정에 있는 모든 사진들 다 가져오기")
    print("4. 종료")
    sel=int(input("> "))
    return sel

if __name__=='__main__':
    GET_IN_TIME=2
    while True:
        sel=intro()
        if sel==4:
            break
        elif sel==1:
            # https://www.instagram.com/p/CNbePKFjxaf/
            print("[+] 원하는 게시글의 URL 을 입력해주세요")
            url=input("input url : ")
            path = "./webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get(url)
            time.sleep(GET_IN_TIME)
            oneMulti.onepost_multi_download(driver,url)
            driver.quit()
        elif sel==2:
            print("[+] 원하는 계정의 URL 을 입력해주세요")
            url=input("input url : ")
            path = "./webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get(url)
            time.sleep(GET_IN_TIME)
            oneacc_multi_thum_download(driver,url)
            driver.quit()
        else:
            print("[-] 올바른 메뉴를 선택해주세요!!!")
    
    



