#autologin bot for school wifi
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import requests

def autologin():
    email = "YOUREMAILHERE"
    password = "YOURPASSWORDHERE"

    browser = webdriver.Firefox()

    browser.get("http://detectportal.firefox.com/canonical.html")

    browser.find_element(By.ID, "inputEmail3").send_keys(email, Keys.ENTER)

    browser.find_element(By.ID, "password").send_keys(password, Keys.ENTER)

    browser.delete_all_cookies()

    browser.close()

    connect()

    time.sleep(1000)

def connect():
    try:
        requests.head("https://example.org/", timeout=1)
        print('Network is active - nothing to do.')
    except requests.ConnectionError:
        print('Network is down. Try to reconnect.')
        autologin()
    time.sleep(10)

while True:
    connect()
