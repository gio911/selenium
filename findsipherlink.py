import math
from selenium import webdriver
import time 

link = 'http://suninjuly.github.io/find_link_text'

sipherLink = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(sipherLink)
try:
    
    browser = webdriver.Chrome()
    browser.get(link)
    codeLink = browser.find_element_by_link_text(sipherLink)
    codeLink.click()
    input1=browser.find_element_by_tag_name('form > div:nth-child(1) > input')
    input1.send_keys("Ivan")
    input2=browser.find_element_by_tag_name('form > div:nth-child(2) > input')
    input2.send_keys("Petrov")
    input3=browser.find_element_by_tag_name('form > div:nth-child(3) > input')
    input3.send_keys("Moscow")
    input4=browser.find_element_by_tag_name('form > div:nth-child(4) > input')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла