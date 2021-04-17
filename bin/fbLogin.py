from selenium.webdriver.common.keys import Keys
def fb_login(driver,is_login_fb,url):
    is_login_fb.click()
    email=input('페북계정 주세요 : ')
    pw=input('비밀번호는요? : ')
    el=driver.find_element_by_id("email")
    el.send_keys(email)
    el=driver.find_element_by_id("pass")
    el.send_keys(pw)
    el.send_keys(Keys.RETURN)
    while(True): # 메인화면으로 돌아왔을때, break 됨
        if(driver.current_url=='https://www.instagram.com/'):
            driver.get(url)
            break