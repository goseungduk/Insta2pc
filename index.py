from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urlREQ
import time, random, string
import sys, os
from bin import onePostMultiPics # 하나의 게시물에서 모든 사진들
from bin import oneAccAllThumbs # 하나의 계정에서 모든 썸네일
from bin import oneAccAllPics # 하나의 계정에서 모든 사진

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
            print("[+] 원하는 게시글의 URL 을 입력해주세요")
            url=input("input url : ")
            path = "./webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get(url)
            time.sleep(GET_IN_TIME)
            onePostMultiPics.onepost_multi_download(driver,url)
            driver.quit()
        elif sel==2:
            print("[+] 원하는 계정의 URL 을 입력해주세요")
            url=input("input url : ")
            path = "./webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get(url)
            time.sleep(GET_IN_TIME)
            oneAccAllThumbs.oneacc_all_thumbs_download(driver,url)
            driver.quit()
        elif sel==3:
            print("[+] 원하는 계정의 URL 을 입력해주세요")
            url=input("input url : ")
            path = "./webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get(url)
            time.sleep(GET_IN_TIME)
            oneAccAllPics.oneacc_all_pics_download(driver,url)
            driver.quit()
        else:
            print("[-] 올바른 메뉴를 선택해주세요!!!")
    
    



