import atexit
import enum
import os
import platform
import time
from typing import List

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

DRIVER_PATH = os.getcwd() + '/driver'


class Helper(object):
    def __init__(self):
        driver_type: DriverType
        sys_type = platform.system()
        if sys_type == 'Darwin':
            if platform.machine() == 'm1':
                driver_type = DriverType.MAC_M1
            else:
                driver_type = DriverType.MAC
        elif sys_type == 'Linux':
            driver_type = DriverType.LINUX
        elif sys_type == 'Windows':
            driver_type = DriverType.WINDOWS
        else:
            print('This system is not supported')
            exit(0)
        print("Platform: " + driver_type.value)
        # self.email: str = input('Email: ')
        # self.password: str = getpass.getpass()
        self.email = 'iliduo@hotmail.com'
        self.password = 'Eric52coco'
        try:
            self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/' + driver_type.value)
            atexit.register(self.exit)
        except SessionNotCreatedException:
            print("Current browser version is not the same as current driver, please check")
            print("Hint: You can goto chrome://settings/help to check your chrome version")
            print("Hint: and goto https://chromedriver.storage.googleapis.com/index.html to download")
            print("Hint: replace " + DRIVER_PATH + '/' + driver_type.value + " with your new driver.")

    def start(self, track: str):
        self.login()
        self.complete(track)

    def login(self):
        self.driver.get('https://app.voxy.com')
        try:
            time.sleep(1)
            self.driver.find_element_by_id('login_form_email_input_field').send_keys(self.email + Keys.ENTER)
            time.sleep(3)
            self.driver.find_element_by_id('password_input_field').send_keys(self.password + Keys.ENTER)
            time.sleep(10)
        finally:
            pass

    def complete(self, track: str):
        self.driver.get('https://app.voxy.com/activities/lesson/by-track/' + track)
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name('practice-button btn btn-primary btn-large theme-primary-button').click()
        finally:
            pass
        self.driver.find_element_by_class_name('start-button btn btn-primary btn-large theme-primary-button').click()


    def find_elements(self, by: By, value: str, wait=1) -> List[WebElement]:
        result = self.driver.find_elements(by, value)
        time.sleep(wait)
        return result

    def exit(self):
        self.driver.quit()


class DriverType(enum.Enum):
    MAC = 'chromedriver_mac'
    MAC_M1 = 'chromedriver_mac_m1'
    LINUX = 'chromedriver_linux'
    WINDOWS = 'chromedriver_windows'
