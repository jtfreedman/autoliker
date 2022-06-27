#!/usr/bin/env python3
import os
import random
from time import sleep
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# get credentials
runMenu = True
while runMenu:
  runType = input("Use env file for credentials? (y/n) ").lower()
  if runType[0] == 'y':
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    userBrowser = os.getenv('BROWSER')
    programChoice = os.getenv('PROG_CHOICE')
  else:
    email = input('Enter email: ')
    password = input('Enter password: ')
    userBrowser = input('Enter your browser: ').lower()
    programChoice = input('Enter L for likes, F for follows: ').lower()

  # instantiates browser
  match userBrowser:
    case 'firefox':
      browser = webdriver.Firefox()
      runMenu = False
    case 'safari':
      browser = webdriver.Safari()
      runMenu = False
    case 'chrome':
      browser = webdriver.Chrome()
      runMenu = False
    case _:
      print('Please choose between Firefox, Safari or Chrome.')

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

# selects newests posts 
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Top: Last Hour']"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='Newest Creations']"))).click()

# continually likes posts so long as there is a visible like button
sleep(3)
match programChoice:
  case 'l':
    while True:
      try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='Like']"))).click()
      except:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      sleep(random.uniform(.7, 1))
  case 'f':
    while True:
      try:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Follow']"))).click()
      except:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
      sleep(random.uniform(.7, 1))