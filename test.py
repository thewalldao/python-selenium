from selenium.webdriver.common.by import By

xpath = "hello %s, %s"
aaa = [1, 1]


def set_dynamic_locator(*paramenter):
    by = xpath % paramenter
    return by


# print(set_dynamic_locator("tuan", "dao"))
print(all(index == 1
          for index in aaa
          ),)
