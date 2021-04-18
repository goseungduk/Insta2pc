import time
from . import downloadIMG as DI
from . import fbLogin as FL
from . import thumbURL as TU
# thumb_urls 필요

def oneacc_all_thumbs_download(driver,url):
    SCROLL_TIME=3
    all_urls=[]
    try:
        is_login_FB=driver.find_element_by_class_name('KPnG0')
    except:
        last_height = driver.execute_script("return document.body.scrollHeight")
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_TIME)
            new_height=driver.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
            all_urls=TU.thumb_urls(driver,'all_thumbs',all_urls)
    else:
        FL.fb_login(driver,is_login_FB,url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_TIME)
            new_height=driver.execute_script("return document.body.scrollHeight")
            if(new_height==last_height):
                break
            last_height=new_height
            all_urls=TU.thumb_urls(driver,'all_thumbs',all_urls)    
    print(all_urls)