import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementPartialLinkText():
    def locate_by_partial_link_text(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com")

        time.sleep(5)

        driver.find_element(By.PARTIAL_LINK_TEXT, "A/B Testi").click()

        time.sleep(5)

        driver.quit()

find_element_partial_link_text = FindElementPartialLinkText()
find_element_partial_link_text.locate_by_partial_link_text()