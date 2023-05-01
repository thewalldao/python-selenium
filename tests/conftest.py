"""
This module contains shared fixture.
"""

import json
import pytest
from selenium import webdriver
from core.driver import Driver
# scope='session' makes
# this fixture run only one time before the entire test suite


def get_config() -> list:
    with open('config.json') as config_file:
        config: list = json.load(config_file)
    return config


# def pytest_itemcollected(item):
#     """ change test name, using fixture names """
#     # item._nodeid = ', '.join(item._fixtureinfo.argnames)
#     item._fixtureinfo.argnames = "hihi"


@pytest.fixture(params=get_config())
def browser(request):
    config: dict = request.param

    Driver.set_driver(config)
    Driver.get_driver()
    # Make its calls wait for elements to appear
    # Driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield Driver.get_driver()

    # Quit the WebDriver instance for the instance
    Driver.quit()
