import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GetElementText():
    def locate_by_element_text(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/checkboxes")

        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Shifting Content").click()

        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "Example 1: Menu Element").click()

        time.sleep(2)

        text_1 = driver.find_element(By.LINK_TEXT, "Home").text

        print(text_1)

        time.sleep(2)

        driver.back()

        time.sleep(2)

        driver.back()

        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "JQuery UI Menus").click()

        time.sleep(2)

        text_2 = driver.find_element(By.LINK_TEXT, "Enabled").text

        time.sleep(2)

        print(text_2)

        time.sleep(2)

        driver.quit()

get_element_text = GetElementText()
get_element_text.locate_by_element_text()