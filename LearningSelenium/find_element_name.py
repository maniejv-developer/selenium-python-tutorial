import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementName():
    def locate_by_name(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.NAME, "username").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_name = FindElementName()
find_element_name.locate_by_name()