from datetime import date
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from parse import parse_clue_list

USER = os.environ['CROSSWORD_USER']
PASS = os.environ['CROSSWORD_PASS']
cwd = os.getcwd()
date_str = date.today().isoformat()

driver = webdriver.Firefox(executable_path='{cwd}/geckodriver.exe'.format(cwd=cwd))
driver.get('https://www.bostonglobe.com/login')

username_element = driver.find_element_by_id('username')
username_element.send_keys(USER)
password_element = driver.find_element_by_id('password')
password_element.send_keys(PASS)
driver.find_element_by_id('mc-login-submit').click()

driver.get('https://www.bostonglobe.com/lifestyle/crossword')

puzzle = driver.find_element_by_id('puzzle')
puzzle.screenshot('{cwd}/{filename}.png'.format(cwd=cwd, filename=date_str))

across_list = driver.find_element_by_id('across')
across_clues = parse_clue_list(across_list)

down_list = driver.find_element_by_id('down')
down_clues = parse_clue_list(down_list)

clues = ['ACROSS'] + across_clues + ['', 'DOWN'] + down_clues
