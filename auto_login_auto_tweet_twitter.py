from selenium import webdriver
from getpass import getpass
import time

usr = input("Phone, email address: ")
pwd = getpass("Password: ")
tweet = input("Enter the message: ")

driver = webdriver.Chrome("../Downloads/chromedriver")
driver.get("https://www.twitter.com/login")

usr_box = driver.find_element_by_css_selector("input.js-username-field.email-input.js-initial-focus")
usr_box.send_keys(usr)
time.sleep(2)

pwd_box = driver.find_element_by_class_name("js-password-field")
pwd_box.send_keys(pwd)
time.sleep(2)

login_btn = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
login_btn.click()
time.sleep(2)

tweet_msg_box = driver.find_element_by_id("tweet-box-home-timeline")
tweet_msg_box.send_keys(tweet)
time.sleep(2)

tweet_btn = driver.find_element_by_css_selector("button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn")
tweet_btn.click()
