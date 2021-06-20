import chromedriver_autoinstaller
from selenium import webdriver
path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)
driver.get('https://www.instagram.com/p/CJ0x92JD51r/')
d=driver.find_element_by_class_name("PyenC")
print(d)