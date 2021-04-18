'''
@ 인스타그램 로그인 루틴(페북계정으로만)
2021.04.18. 최종수정
'''

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
    while(True):
        if(driver.current_url=='https://www.instagram.com/'):
            driver.get(url)
            break