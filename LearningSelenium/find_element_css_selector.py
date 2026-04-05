import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementCSSSelector():
    def locate_by_css_selector(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_css_selector = FindElementCSSSelector()
find_element_css_selector.locate_by_css_selector()