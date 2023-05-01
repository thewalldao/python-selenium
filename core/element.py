from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import selenium.webdriver as webdriver
from selenium.webdriver.support.wait import WebDriverWait
from core.driver import Driver
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from selenium.common.exceptions import TimeoutException
import utils.constant as Constant
import sys


class Element:
    def __init__(self, xpath: str = None, css: str = None):
        self.driver = Driver.get_driver()
        self.parameter = None

        if xpath:
            self.xpath: str = xpath
            self.locator: str = xpath
            self.by: By = By.XPATH
        else:
            self.css: str = css
            self.locator: str = css
            self.by: By = By.CSS_SELECTOR

    def set_dynamic_locator(self, *paramenter):
        self.locator = self.xpath % paramenter
        return self

    def get_element(self) -> WebElement:
        if self.xpath:
            return self.driver.find_element(self.by, self.locator)
        else:
            return self.driver.find_element(self.by, self.css)

    def get_element_list(self) -> List[WebElement]:
        if self.xpath:
            return self.driver.find_elements(self.by, self.locator)
        else:
            return self.driver.find_elements(self.by, self.css)

    def waitForPresence(self, timeout=Constant.WAIT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda condition:
                len(self.get_element_list()) != 0,
                f"""
                Timeout with {timeout}s
                Locator: "{self.locator}" is not presented
                """
            )
        except TimeoutException:
            tb = sys.exc_info()[2]
            print(tb.__class__())

    def waitForDisplayed(self, timeout=Constant.WAIT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda condition:
                len(self.get_element_list()) != 0 and
                self.get_element().is_displayed(),
                f"""
                Timeout with {timeout}s
                Locator: "{self.locator}" is not Displayed
                """
            )
        except TimeoutException:
            tb = sys.exc_info()[2]
            print(tb.__class__())

    def waitForClickAble(self, timeout=Constant.WAIT_TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda condition:
                len(self.get_element_list()) != 0 and
                self.get_element().is_displayed() and
                self.get_element().is_enabled(),
                f"""
                Timeout with {timeout}s
                Locator: "{self.locator}" is not Clickable
                """
            )
        except TimeoutException:
            tb = sys.exc_info()[2]
            print(tb.__class__())

    def click(self, timeout=Constant.WAIT_TIMEOUT):
        self.waitForClickAble(timeout)
        self.get_element().click()

    def send_keys(self, value, timeout=Constant.WAIT_TIMEOUT):
        self.waitForDisplayed(timeout)
        self.get_element().send_keys(value)

    def get_attribure(self, attributeName) -> str:
        return self.get_element().get_attribute(attributeName)
