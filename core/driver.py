
import selenium.webdriver as webdriver
from core.factory import Factory


class Driver:
    driver = None

    def __init__(self):
        pass

    @staticmethod
    def get_driver():
        return Driver.driver

    @staticmethod
    def set_driver(config):
        Driver.driver = Factory.get_config(config)

    @staticmethod
    def get(url: str):
        Driver.driver.get(url)

    @staticmethod
    def title():
        return Driver.driver.title

    @staticmethod
    def close():
        Driver.driver.close()

    @staticmethod
    def quit():
        Driver.driver.quit()

    @staticmethod
    def implicitly_wait(time_to_wait: float):
        Driver.driver.implicitly_wait(time_to_wait)
