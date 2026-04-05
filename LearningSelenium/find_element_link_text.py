import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementLinkText():
    def locate_by_link_text(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com")

        time.sleep(5)

        driver.find_element(By.LINK_TEXT, "A/B Testing").click()

        time.sleep(5)

        driver.quit()

find_element_link_text = FindElementLinkText()
find_element_link_text.locate_by_link_text()