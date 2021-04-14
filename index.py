from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urlREQ
import time, random, string
from bin import oneMulti

def thumb_urls(driver): # 썸네일 url 따오기
    thumbs=driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w')
    for thumb in thumbs:
        link=thumb.find_elements_by_tag_name('a')
        print(link[0].get_attribute('href'))



def oneacc_multi_thum_download(driver,url):
    #aria-label="제어"
    collecting_urls(driver,url)

def collecting_urls(driver,url):
    # https://www.instagram.com/dlwlrma/
    # https://www.instagram.com/accounts/signup/
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except: # 익명으로 로그인이 무사히 되었을 때
        # 스크롤 작업 추가 '21.04.14.
        thumb_urls(driver)
    else: # 익명로그인이 잘 안되었을때
        # fb login 작업 진행
        is_login_FB.click()
        el=driver.find_element_by_id("email")
        el.send_keys("email")
        el=driver.find_element_by_id("pass")
        el.send_keys("pass")
        el.send_keys(Keys.RETURN)
        while(True): # 메인화면으로 돌아왔을때, break 됨
            if(driver.current_url=='https://www.instagram.com/'):
                driver.get(url)
                break
        thumb_urls(driver)

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
            if(driver):
                driver.quit()
            break
        elif sel==1:
            print("[+] 원하는 게시글의 URL 을 입력해주세요")
            url=input("input url : ")
            path = "./webdriver/chromedriver.exe"
            driver = webdriver.Chrome(path)
            driver.get(url)
            time.sleep(GET_IN_TIME)
            oneMulti.onepost_multi_download(driver)
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
    
    



