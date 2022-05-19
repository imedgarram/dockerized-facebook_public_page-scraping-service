from selenium import webdriver
import time
from bs4 import BeautifulSoup
import json
from selenium.webdriver import DesiredCapabilities

#driver settings
chrome_options = DesiredCapabilities.CHROME
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
chrome_options['prefs'] = prefs

#remote connection to selenium container
driver = webdriver.Remote(command_executor="http://selenium:4444/wd/hub",

                             desired_capabilities=chrome_options)
driver.get("https://www.facebook.com/Reuters")

def get_post(article):

    """get_post is a helper function that parse drive.page_source and scrap posts"""

    post = article.find('div',class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q')
    if post:
        return post.text
    else:
        return ''
def get_comments(article):
    
    """ get_comments is a helper function that gather comments"""

    comment=[]
    comments=article.findAll('div',class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql")
    for elt in comments:
        comment.append(elt.text)
    return comment





def scraping():
    """scraping function scrap data from reuters facebook publoc page"""
    scraped_data=[]
    #scrolling block
    i = 0
    while i < 50: 
        SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
        # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                i+=1
                break
            last_height = new_height
    html = BeautifulSoup(driver.page_source,'lxml') # page_source of reuters facebook public page

    for article in html.findAll('div',class_="rq0escxv l9j0dhe7 du4w35lb"):
        post=get_post(article)
        comments=get_comments(article)
        scraped_data.append({'reuters_post':post,"post_comments":comments})

    return scraped_data



    
    




  




