from selenium import webdriver
from getpass import getpass

usr = input("Username or email address: ")
pwd = getpass("Password: ")

driver = webdriver.Chrome("/home/afzaal/Downloads/chromedriver")
driver.get("https://github.com/login")

username_box = driver.find_element_by_id("login_field")
username_box.send_keys(usr)

password_box = driver.find_element_by_id("password")
password_box.send_keys(pwd)

sign_in_btn = driver.find_element_by_name("commit")
sign_in_btn.submit()
