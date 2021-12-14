from selenium import webdriver
import chromedriver_autoinstaller
import sys
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(chromedriver_autoinstaller.install())

driver.get("https://www.instagram.com/dlwlrma/")
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
time.sleep(2)
is_login_FB=driver.find_element_by_class_name('KPnG0')
print(is_login_FB)
fb_login(driver,is_login_FB,"https://www.instagram.com/dlwlrma/","01091680506","ahfmrksk!@96")
# find_elements_by_* is deprecated
#moreBTN=driver.find_elements_by_css_selector("#react-root > div > div > section > main > div > div._2z6nI > div.qF0y9.Igw0E.rBNOH.eGOV_._4EzTm > div > button > div")
#thumbs=driver.find_elements_by_css_selector('#react-root > div > div > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(2)')
thumbs=driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w')
print(len(thumbs))

