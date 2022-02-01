from time import time
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1=int(browser.find_element_by_id('num1').text)
    num2=int(browser.find_element_by_id('num2').text)
    sum = num1+num2
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum))
    btn=browser.find_element_by_tag_name('button')
    btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
