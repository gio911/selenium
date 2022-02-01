import time
import math
from selenium import webdriver

link="http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x=browser.find_element_by_id('input_value').text
    answer=calc(int(x))
    input = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(answer)
    chb=browser.find_element_by_id('robotCheckbox')
    chb.click()
    rr=browser.find_element_by_id('robotsRule')
    rr.click()
    btn=browser.find_element_by_tag_name('button')
    btn.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()    