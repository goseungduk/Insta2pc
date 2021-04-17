import time
from . import downloadIMG as DI
from . import fbLogin as FL
# searching and download pics
# 동적으로 따올만한 방법 구상 필요
def onepost_multi_download(driver,url):
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except:
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
            DI.download_img(pic2.get_attribute('src'))
            if(i!=len(pic_count)-1):
                pic_arrow.click()
            time.sleep(1)
    else:
        FL.fb_login(driver,is_login_FB,url)
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
            DI.download_img(pic2.get_attribute('src'))
            if(i!=len(pic_count)-1):
                pic_arrow.click()
            time.sleep(1)