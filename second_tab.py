import time, math
from selenium import webdriver

link = 'http://suninjuly.github.io/redirect_accept.html'
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_tag_name('button')
    btn.click()
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(answer)
    btn = browser.find_element_by_tag_name('button')
    btn.click()

finally:
    time.sleep(30)
    browser.quit()