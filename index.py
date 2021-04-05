from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request as urlREQ
import time, random, string
from bin import oneMulti

def oneacc_multi_thum_download(driver,url):
    #aria-label="제어"
    #class="v1Nh3 kIKUG  _bz0w" -> a 태그
    collecting_urls(driver,url)

def collecting_urls(driver,url):
    # https://www.instagram.com/dlwlrma/
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except: # 익명으로 로그인이 무사히 되었을 때
        # 게시물들 URL 긁어오기 && 스크롤 작업 추가
        article=driver.find_element_by_class_name("ySN3v")
        first=article.find_element_by_xpath("/div[1]/div[1]/div[1]")
        second=first.find_element_by_tag_name("a")
        print(second.get_attribute('href'))
        print('keep going')
    else: # 익명로그인이 잘 안되었을때
        # fb login 작업 진행
        is_login_FB.click()
        el=driver.find_element_by_id("email")
        el.send_keys("email")
        el=driver.find_element_by_id("pass")
        el.send_keys("pass")
        el.send_keys(Keys.RETURN)
        while(True):
            if(driver.current_url=="https://www.instagram.com/"):
                driver.get(url)
                break
        article=driver.find_element_by_class_name("ySN3v")
        first=article.find_element_by_xpath("/div[1]/div[1]/div[1]")
        second=first.find_element_by_tag_name("a")
        print(second.get_attribute('href'))
        # driver.get(url) 로그인하고 메인화면으로 넘어오는거 어떻게 해결해!?
        print('good')
     
    #res=driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w')
    #print(res)

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
    
    



