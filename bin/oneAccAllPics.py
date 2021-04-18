'''
@ 하나의 계정에서 모든 사진가져오기
2021.04.18. 최종수정
'''
import time
from . import downloadIMG as DI
from . import fbLogin as FL
from . import thumbURL as TU

def oneacc_all_pics_download(driver,url):
    all_urls=[]
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except:
        last_height= driver.execute_script("return document.body.scrollHeight")
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height=driver.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
            TU.thumb_urls(driver,'all_pics',all_urls)
    else:
        FL.fb_login(driver,is_login_FB,url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height=driver.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
            TU.thumb_urls(driver,'all_pics',all_urls)
    
