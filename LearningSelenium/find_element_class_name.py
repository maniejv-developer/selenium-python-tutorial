import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementClassName():
    def locate_by_class_name(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.NAME, "username").send_keys("tomsmith")

        time.sleep(5)

        driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

        time.sleep(5)

        driver.find_element(By.CLASS_NAME, "radius").click()

        time.sleep(5)

        driver.quit()

find_element_class_name = FindElementClassName()
find_element_class_name.locate_by_class_name()