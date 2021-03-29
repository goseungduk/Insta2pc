from selenium import webdriver
import urllib.request as urlREQ
import time
import random
import string

# downloading pics with src
def download_img(url):
    tmp=''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
    urlREQ.urlretrieve(url,"test"+tmp+".jpg")

# searching and download pics
# 동적으로 따올만한 방법 구상 필요
def multi_download(driver):    
    # extracting pics count
    pic_count=driver.find_element_by_xpath("//div[@class='JSZAJ  _3eoV-  IjCL9  WXPwG ']").find_elements_by_tag_name("div")

    # extracting next button
    pic_arrow=driver.find_element_by_xpath("//button[@tabindex='-1']")
    
    for i in range(0,len(pic_count)):
        if(i==0): # start point
            if(len(pic_count)>5): # temporary number 5
                p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
            else:
                p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]")
        else:
            try:
                p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/div[1]")
            except:
                p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/div[1]/div[1]/div[1]/div[1]")
        pic2=p.find_element_by_tag_name("img")
        download_img(pic2.get_attribute('src'))
        if(i!=len(pic_count)-1):
            pic_arrow.click()
        time.sleep(1)

def intro():
    print("<인스타그램 사진 다운로더>")
    print("1. 하나의 게시글에 있는 모든 사진 가져오기")
    print("2. 하나의 계정에 있는 모든 썸네일사진 가져오기")
    print("3. 하나의 계정에 있는 모든 사진들 다 가져오기")
    print("4. 종료")
    sel=int(input("> "))
    return sel

if __name__=='__main__':
    # driver.get("https://www.instagram.com/p/CMY7VtJFo-6/") # shoe_prize 6 pics
    # driver.get("https://www.instagram.com/p/CMYmpH_ppSQ/") # shoe_prize 10 pics
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
            multi_download(driver)
            driver.quit()
        else:
            print("[-] 올바른 메뉴를 선택해주세요!!!")
    

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    
    



