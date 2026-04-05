import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementTagName():
    def locate_by_tag_name(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.TAG_NAME, "input").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_tag_name = FindElementTagName()
find_element_tag_name.locate_by_tag_name()