#autologin bot for school wifi
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import requests

def autologin():
    email = "USERNAME"
    password = "PASSWORD"

    options = FirefoxOptions()

    options.add_argument("--headless")

    browser = webdriver.Firefox(options=options)

    # browser = webdriver.Firefox()

    browser.get("http://detectportal.firefox.com/canonical.html")

    browser.find_element(By.ID, "inputEmail3").send_keys(email, Keys.ENTER)

    browser.find_element(By.ID, "password").send_keys(password, Keys.ENTER)

    browser.delete_all_cookies()

    browser.close()

    time.sleep(5)

while (True):
    try:
        requests.head("https://example.org/", timeout=1)
        print('Network is active - nothing to do.')
        time.sleep(100)
    except requests.ConnectionError:
        print('Network is down. Try to reconnect.')
        autologin()
