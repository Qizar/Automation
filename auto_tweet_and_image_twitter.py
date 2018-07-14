from selenium import webdriver
from getpass import getpass
import time

usr = input("Enter username or email id: ")
pwd = getpass("Password: ")
msg = input("Enter the tweet: ")
img = input("Enter the image URL: ")

driver = webdriver.Chrome("/home/afzaal/Downloads/chromedriver")
driver.get("https://www.twitter.com/login")
time.sleep(2)

usr_box = driver.find_element_by_class_name("js-username-field")
usr_box.send_keys(usr)
time.sleep(2)

pwd_box = driver.find_element_by_class_name("js-password-field")
pwd_box.send_keys(pwd)
time.sleep(2)

login_btn = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
login_btn.click()
time.sleep(2)

img_btn = driver.find_element_by_css_selector("input.file-input.js-tooltip")
img_btn.send_keys(img)
time.sleep(2)

msg_box = driver.find_element_by_id("tweet-box-home-timeline")
msg_box.send_keys(msg)

tweet_send = driver.find_element_by_css_selector("button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn")
tweet_send.click()
