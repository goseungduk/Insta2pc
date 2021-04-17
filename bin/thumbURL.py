
def thumb_urls(driver,mode,all_urls): # 썸네일 url 따오기
    if(mode=="all_pics"):
        thumbs=driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w')
        for thumb in thumbs:
            link=thumb.find_elements_by_tag_name('a')[0].get_attribute('href')
            if(link not in all_urls):
                all_urls.append(link)
    else:
        # <div class="KL4Bh"> 를 찾는 코드 넣기
        thumbs=driver.find_elements_by_class_name('KL4Bh')
        for thumb in thumbs:
            src=thumb.find_elements_by_tag_name('img')[0].get_attribute('src')
            if(src not in all_urls):
                all_urls.append(src)
    return all_urls