import time
from selenium import webdriver
import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector('[name=firstname]')
    first_name.send_keys('David')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Stroitel')
    email = browser.find_element_by_name('email')
    email.send_keys('david@mail.ru')
    dir_path=os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, 'bio.txt')
    choose_file=browser.find_element_by_name('file')
    choose_file.send_keys(file_path)
    btn = browser.find_element_by_tag_name('button')
    btn.click()
finally:
    time.sleep(30)
    browser.quit()