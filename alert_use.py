import time
from selenium import webdriver
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_tag_name('button')
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(answer)
    btn = browser.find_element_by_tag_name('button')
    btn.click()


finally:
    time.sleep(20)
    browser.quit()