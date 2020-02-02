#!

# commandLineEmailer.py - by adding a yahoo email address and password,
# commandLineEmailer can send an email using command line arguments. This
# can be forward utilized and used using "winkey + R" to use this code
# through the windows "Run" window

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


emailAddress = sys.argv[1]
emailText = ' '.join(sys.argv[4:])
yahooEmailAddress = sys.argv[2]
yahooEmailPass = sys.argv[3]


browser = webdriver.Firefox()
browser.get('https://login.yahoo.com?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd')
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys(yahooEmailAddress)
emailElem.submit()
time.sleep(5)
passwordelem = browser.find_element_by_id('login-passwd')
passwordelem.send_keys(yahooEmailPass)
passwordelem.send_keys(Keys.RETURN)
time.sleep(7)


composeButton = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div[1]/nav/div/div[1]/a')
composeButton.send_keys(Keys.RETURN)
time.sleep(5)

toBox = browser.find_element_by_xpath('//*[@id="message-to-field"]')
toBox.send_keys(emailAddress)
subjectBox = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/div/input')
subjectBox.send_keys('test')
textBox = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/div[2]/div/div[1]')
textBox.send_keys(emailText)
sendButton = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/button')
sendButton.send_keys(Keys.RETURN)
