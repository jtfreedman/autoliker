#!/usr/bin/env python3
from time import sleep
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# instantiates firefox
browser = webdriver.Firefox()
browser.implicitly_wait(5)

# opens firefox to link
browser.get('https://creator.nightcafe.studio/feed')

# clicks on login by password and logs in
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Connect with password']"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='email']"))).send_keys('USERNAME')
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='password']"))).send_keys('PASSWORD')
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Log in']"))).click()

# waits for page to load and then navigates to feed
sleep(3)
browser.get('https://creator.nightcafe.studio/explore')
sleep(3)

# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//button[@class='css-ifoe43']"))).click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Top: Last Hour']"))).click()
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='Newest Creations']"))).click()
# continually likes posts so long as there is a visible like button
sleep(3)
while (2 > 1):
  WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Follow']"))).click()
  try:
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, f"//button[@title='Like']"))).click()
  except:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  sleep(.75)

#browser.close()