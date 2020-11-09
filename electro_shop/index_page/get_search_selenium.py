from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



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
    sitename=[]

    images = driver.find_elements_by_xpath("//div/div/a/div/div/img[@src]")
    price = driver.find_elements_by_xpath("//div/span/span/span[contains(text(), 'PLN')]")
    link = driver.find_elements_by_xpath("//div/div/a[contains(@class,'merchant-name')][@href]")
    name = driver.find_elements_by_xpath("//div/div/div/a/h3")
    time.sleep(10)
    for n in name:
        text = n.text
        names.append(text)
    for p in price:
        text = p.text
        money.append(text)
    for l in link:
        text = l.get_attribute("href")
        links.append(text)
    for l1 in link:
        text=l1.text
        sitename.append(text)
    for image in images:
        img = image.get_attribute('src')
        im.append(img)
    price_list = [i for i in money if i]
    links_list = [i for i in links if i]
    im_list = [i for i in im if i]
    names_list = [i for i in names if i]
    mydict = zip(price_list, links_list, im_list, names_list,sitename)
    driver.close()
    return mydict


# search_selenium('STM32F4')
