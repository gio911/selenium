import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input = browser.find_element_by_id('answer')
    x=browser.find_element_by_id('treasure').get_attribute('valuex')
    input.send_keys(calc(x))
    chb=browser.find_element_by_id('robotCheckbox')
    chb.click()
    rb=browser.find_element_by_id('robotsRule')
    rb.click()
    btn=browser.find_element_by_css_selector('button.btn')
    btn.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


