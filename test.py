from selenium.webdriver.common.by import By

xpath = "hello %s, %s"


def set_dynamic_locator(*paramenter):
    by = xpath % paramenter
    return by


print(set_dynamic_locator("tuan", "dao"))
print(xpath)
