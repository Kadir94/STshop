from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time


def search_selenium(elem):
    path = r"C:\Users\kdr34\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get('https://www.google.com/shopping')
    search = driver.find_element_by_name('q')
    search.send_keys(elem)
    search.send_keys(Keys.RETURN)

    company_name = []
    im = []

    result2 = driver.find_elements_by_class_name("IHk3ob")
    images = driver.find_elements_by_tag_name('img')

    time.sleep(2)

    for c in result2:
        text = c.text
        rest = re.sub('^.*?\n', '', text)
        company_name.append(rest)

    for image in images:
        img = image.get_attribute('src')
        im.append(img)

    mydict = dict(zip(company_name, im))
    return mydict

