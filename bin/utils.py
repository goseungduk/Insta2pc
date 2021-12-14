from selenium.webdriver.common.keys import Keys
import urllib.request as urlREQ
import random, string, time

def lazy(t):
    time.sleep(t)

# downloading pics with src
def download_img(url):
    tmp=''.join([random.choice(string.ascii_lowercase) for _ in range(5)])
    urlREQ.urlretrieve(url,"test"+tmp+".jpg")

"""
    인스타그램 로그인 루틴(페북계정으로만)
    Args:
        Web Driver
        URL
        FACEBOOK ID
        FACEBOOK PW
"""
def fb_login(driver,url,id,pw):
    print(url)
    driver.get(url)
    lazy(3)
    try:
        # 인스타 게시물은 보이는데 로그인 안되있는 상태
        login_btn=driver.find_element_by_css_selector("#react-root > div > div > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > span > a:nth-child(1)")
    except:
        # 인스타 게시물도 안보이고 로그인도 안되어있는 상태
        try:
            login_fb=driver.find_element_by_class_name('KPnG0')
            login_fb.click()
            email=id
            pw=pw
            el=driver.find_element_by_id("email")
            el.send_keys(email)
            el=driver.find_element_by_id("pass")
            el.send_keys(pw)
            lazy(10)
            el.send_keys(Keys.RETURN)
            lazy(10)
            driver.get(url) # 가야하는 url 로 이동
        except:
            print("pass")
    else:
        login_btn.click()
        lazy(3)
        login_fb=driver.find_element_by_class_name('KPnG0')
        login_fb.click()
        email=id
        pw=pw
        el=driver.find_element_by_id("email")
        el.send_keys(email)
        el=driver.find_element_by_id("pass")
        el.send_keys(pw)
        lazy(10)
        el.send_keys(Keys.RETURN)
        lazy(10)
        driver.get(url) # 가야하는 url 로 이동

"""
    인스타그램 썸네일 url 따오는 함수
    Args:
        Web Driver
        Mode : 썸네일 url만 가져올지 아니면 모든 사진 다운을 위해 게시물 url을 가져올지 여부
        All_urls : 수집한 게시물 url 리스트
"""
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
                all_urls.append(src)
    return all_urls
