# Test Case
# ------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

from selenium import webdriver
import selenium.webdriver.common.selenium_manager as selenium_manager
from selenium.webdriver.chrome.service import Service
from core.element import Element
from core.driver import Driver
import logging

LOGGER = logging.getLogger(__name__)
# def test_second(browser):

#     Driver.get("https://opensource-demo.orangehrmlive.com/")
#     Element(xpath="//input[@name='username']").send_keys("Admin")
#     Element(xpath="//input[@name='password']").send_keys("admin123")
#     Element(xpath="//button").click()

#     act_title = Driver.title()
#     exp_title = "OrangeHRM"
#     assert act_title == exp_title


def test_first(browser):
    # logging.basicConfig(level=logging.DEBUG)
    # LOGGER.info(selenium_manager.SeleniumManager().driver_location())
    input_xpath = "//input[@name='%s']"
    LOGGER.info("Goto https://opensource-demo.orangehrmlive.com/")
    Driver.get("https://opensource-demo.orangehrmlive.com/")

    LOGGER.info("Filling Username Field")
    Element(xpath=input_xpath).set_dynamic_locator(
        "username").send_keys("Admin")

    LOGGER.info("Filling Passworf Field")
    Element(xpath=input_xpath).set_dynamic_locator(
        "password").send_keys("admin123")

    LOGGER.info("Click to Button")
    Element(xpath="//button").click()

    act_title = Driver.title()
    exp_title = "OrangeHRM"
    assert act_title == exp_title
