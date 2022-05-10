import atexit
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

DRIVER_PATH = '/Users/eric/Projects/python/click_helper/driver/driver'


class Helper(object):
    def __init__(self):
        service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        atexit.register(self.exit)

    def start(self):
        self.driver.get('https://app.voxy.com')
        time.sleep(3)
        self.login('iliduo@hotmail.com', 'eric52coco')

    def login(self, email: str, password: str):
        self.driver.find_element(By.ID, 'login_form_email_input_field').send_keys(email)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'voxy-button__text').click()
        time.sleep(2)
        self.driver.find_element(By.ID, 'password_input_field').send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'voxy-button__text').click()

    def exit(self):
        self.driver.quit()
