from tabnanny import verbose
from selenium import webdriver
import time


link = 'http://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link)
    btn = browser.find_elements_by_id('button')
finally:
    time.sleep(30)
    browser.quit()  
    
      