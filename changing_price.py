from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    # price = browser.find_element_by_id('price').text
    btn = browser.find_element_by_tag_name('button')

    #browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    btn.click()

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    input = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(answer)
    btn_s = browser.find_element_by_id('solve')
    btn_s.click()
    
    
finally:
    time.sleep(30)
    browser.quit()

    