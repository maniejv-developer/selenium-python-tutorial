import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementId():
    def locate_by_id(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.ID, "username").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_id = FindElementId()
find_element_id.locate_by_id()