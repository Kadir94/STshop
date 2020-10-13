from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import itertools


def search_selenium(elem):
    path = r"C:\Users\kdr34\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get('https://www.google.com/shopping')
    search = driver.find_element_by_name('q')
    search.send_keys(elem)
    search.send_keys(Keys.RETURN)

    money = []
    im = []
    links = []
    names = []

    images = driver.find_elements_by_class_name('TL92Hc')
    price = driver.find_elements_by_class_name("Nr22bf")
    link = driver.find_elements_by_class_name("hy2WroIfzrX__merchant-name")
    name = driver.find_elements_by_class_name("xsRiS")
    time.sleep(4)
    for n in name:
        text = n.text
        names.append(text)
    for p in price:
        text = p.text
        money.append(text)
    for l in link:
        text = l.get_attribute("href")
        links.append(text)
    for image in images:
        img = image.get_attribute('src')
        im.append(img)
    mydict = zip(money, links, im, names)
    return mydict
