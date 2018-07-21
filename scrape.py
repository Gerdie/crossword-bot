import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USER = os.environ['CROSSWORD_USER']
PASS = os.environ['CROSSWORD_PASS']
cwd = os.getcwd()

driver = webdriver.Chrome(executable_path='{cwd}/chromedriver.exe'.format(cwd=cwd))
driver.get('https://www.bostonglobe.com/login')

usernameElement = driver.find_element_by_id('username')
usernameElement.send_keys(USER)
passwordElement = driver.find_element_by_id('password')
passwordElement.send_keys(PASS)
driver.find_element_by_id('mc-login-submit').click()

driver.get('https://www.bostonglobe.com/lifestyle/crossword')
