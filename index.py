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

print("<인스타그램 사진 다운로더>")
print("※ 당분간은 사진 여러장 다운만 가능합니다.")
print("- 사진여러장 있는 게시글의 URL 을 넣으시면 됩니다.")
url=input("input url : ")
# print("- 웹드라이버 경로를 입력해주세요.")
# path=input("input webdriver path : ")
options = webdriver.ChromeOptions()
options.add_argument('headless')
path = "./webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get(url)
# driver.get("https://www.instagram.com/p/CMY7VtJFo-6/") # shoe_prize 6 pics
# driver.get("https://www.instagram.com/p/CMYmpH_ppSQ/") # shoe_prize 10 pics
time.sleep(2)

multi_download(driver)

driver.quit()
    



