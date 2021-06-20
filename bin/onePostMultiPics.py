'''
@ 하나의 게시물에서 모든 사진가져오기
2021.04.18. 최종수정
'''

import time
from bin.utils import download_img, fb_login

def onepost_multi_download(driver,url,id=None,pw=None):
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except:
        # 게시물의 사진개수 추출
        try:
            pic_count=driver.find_element_by_xpath("//div[@class='JSZAJ   _3eoV-  IjCL9  WXPwG ']").find_elements_by_tag_name("div")
            pic_arrow=driver.find_element_by_xpath("//button[@tabindex='-1']")
        except:
            # 사진하나만 있을때
            try:
                driver.find_element_by_class_name("PyenC")
            except:
                p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]")
                pic=p.find_element_by_tag_name("img")
                download_img(pic.get_attribute('src'))
                time.sleep(1)
            else:
                return 0
        else:
            for i in range(0,len(pic_count)):
                pics=driver.find_elements_by_class_name("Ckrof")
                if(i==0):
                    try:
                        p=pics[0].find_element_by_class_name("PyenC")
                    except:
                        p=pics[0].find_element_by_class_name("KL4Bh")
                        pic=p.find_element_by_tag_name("img")
                        download_img(pic.get_attribute('src'))
                else:
                    try:
                        p=pics[1].find_element_by_class_name("PyenC")
                    except:
                        p=pics[1].find_element_by_class_name("KL4Bh")
                        pic=p.find_element_by_tag_name("img")
                        download_img(pic.get_attribute('src'))
                if(i!=len(pic_count)-1):
                    pic_arrow.click()
                    time.sleep(1)
                else:
                    continue
    else:
        fb_login(driver,is_login_FB,url,id,pw)
        # 게시물의 사진개수 추출
        try:
            pic_count=driver.find_element_by_xpath("//div[@class='JSZAJ   _3eoV-  IjCL9  WXPwG ']").find_elements_by_tag_name("div")
            pic_arrow=driver.find_element_by_xpath("//button[@tabindex='-1']")
        except:
            # 사진하나만 있을때
            try:
                driver.find_element_by_class_name("PyenC")
            except:
                p=driver.find_element_by_xpath("//div[1]/section[1]/main[1]/div[1]/div[1]/article[1]/div[2]/div[1]/div[1]/div[1]")
                pic=p.find_element_by_tag_name("img")
                download_img(pic.get_attribute('src'))
                time.sleep(1)
            else:
                return 0
                
        else:
            for i in range(0,len(pic_count)):
                pics=driver.find_elements_by_class_name("Ckrof")
                if(i==0):
                    try:
                        p=pics[0].find_element_by_class_name("PyenC")
                    except:
                        p=pics[0].find_element_by_class_name("KL4Bh")
                        pic=p.find_element_by_tag_name("img")
                        download_img(pic.get_attribute('src'))
                else:
                    try:
                        p=pics[1].find_element_by_class_name("PyenC")
                    except:
                        p=pics[1].find_element_by_class_name("KL4Bh")
                        pic=p.find_element_by_tag_name("img")
                        download_img(pic.get_attribute('src'))
                if(i!=len(pic_count)-1):
                    pic_arrow.click()
                    time.sleep(1)
                else:
                    continue