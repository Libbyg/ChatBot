from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("D:/chromedriver")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait (browser, 600)

target ='"name"'
string = "some message"
x_args = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_args)))
target.click()

input_box= browser.find_element_by_class_name('_1Plpp')
for i in range (2):
    input_box.send_keys(string + Keys.ENTER)
