import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementXPath():
    def locate_by_xpath(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.XPATH, "//input[@id='username']").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_xpath = FindElementXPath()
find_element_xpath.locate_by_xpath()