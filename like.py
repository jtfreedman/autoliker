#!/usr/bin/env python3
import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# get credentials
runType = input("Use env file for credentials? (y/n)").lower()
if runType[0] == 'y':
  load_dotenv()
  email = os.getenv('EMAIL')
  password = os.getenv('PASSWORD')
  userBrowser = os.getenv('BROWSER')
else:
  email = input('Enter email: ')
  password = input('Enter password: ')
  userBrowser = input('Enter your browser: ').lower()

# instantiates browser
match userBrowser:
  case 'firefox':
    browser = webdriver.Firefox()
  case 'safari':
    browser = webdriver.Safari()
  case 'chrome':
    browser = webdriver.Chrome()
  case _:
    print('Your input is not compatibile.')
    quit()

browser.implicitly_wait(5)

# opens browser to particular link
browser.get('https://creator.nightcafe.studio/feed')

# clicks on login by password and logs in
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Connect with password']"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='email']"))).send_keys(email)
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='password']"))).send_keys(password)
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Log in']"))).click()

# waits for page to load and then navigates to specific feed
sleep(3)
browser.get('https://creator.nightcafe.studio/explore')
sleep(3)

# selects newests posts 
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Top: Last Hour']"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='Newest Creations']"))).click()

# continually likes posts so long as there is a visible like button
sleep(3)
while (2 > 1):
  WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='Like']"))).click()
  sleep(.75)