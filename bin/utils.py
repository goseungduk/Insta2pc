'''
@ 게시물에서 사진따오기
'''
from selenium.webdriver.common.keys import Keys
import urllib.request as urlREQ
import random, string
# downloading pics with src
def download_img(url):
    tmp=''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
    urlREQ.urlretrieve(url,"test"+tmp+".jpg")

'''
@ 인스타그램 로그인 루틴(페북계정으로만)
'''
def fb_login(driver,is_login_fb,url,id,pw):
    is_login_fb.click()
    email=id
    pw=pw
    el=driver.find_element_by_id("email")
    el.send_keys(email)
    el=driver.find_element_by_id("pass")
    el.send_keys(pw)
    el.send_keys(Keys.RETURN)
    while(True):
        if(driver.current_url=='https://www.instagram.com/'):
            driver.get(url)
            break

'''
@ 인스타그램 썸네일 url 따오기
'''
def thumb_urls(driver,mode,all_urls): # 썸네일 url 따오기
    if(mode=="all_pics"):
        thumbs=driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w')
        for thumb in thumbs:
            link=thumb.find_elements_by_tag_name('a')[0].get_attribute('href')
            if(link not in all_urls):
                all_urls.append(link)
    else:
        thumbs=driver.find_elements_by_class_name('KL4Bh')
        for thumb in thumbs:
            src=thumb.find_elements_by_tag_name('img')[0].get_attribute('src')
            if(src not in all_urls):
                print(src)
                all_urls.append(src)
    return all_urls