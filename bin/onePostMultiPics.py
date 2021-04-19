'''
@ 하나의 게시물에서 모든 사진가져오기
2021.04.18. 최종수정
'''

import time
from bin.utils import download_img, fb_login

def onepost_multi_download(driver,url):
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except:
        # 게시물의 사진개수 추출
        try:
            pic_count=driver.find_element_by_xpath("//div[@class='JSZAJ  _3eoV-  IjCL9  WXPwG ']").find_elements_by_tag_name("div")
            pic_arrow=driver.find_element_by_xpath("//button[@tabindex='-1']")
        except:
            # 사진하나만 있을때
            p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]")
            pic2=p.find_element_by_tag_name("img")
            download_img(pic2.get_attribute('src'))
            time.sleep(1)
        else:
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
    else:
        fb_login(driver,is_login_FB,url)
       # 게시물의 사진개수 추출
        try:
            pic_count=driver.find_element_by_xpath("//div[@class='JSZAJ  _3eoV-  IjCL9  WXPwG ']").find_elements_by_tag_name("div")
            pic_arrow=driver.find_element_by_xpath("//button[@tabindex='-1']")
        except:
            # 사진하나만 있을때
            p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]")
            pic2=p.find_element_by_tag_name("img")
            download_img(pic2.get_attribute('src'))
            time.sleep(1)
        else:
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