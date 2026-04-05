import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementsList():
    def locate_by_elements_list(self):
        driver = webdriver.Chrome()

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com")

        time.sleep(5)

        tag_names = driver.find_elements(By.TAG_NAME, "a")

        time.sleep(5)

        print(len(tag_names))

        time.sleep(5)

        for tag in tag_names:
            print(tag.text)

        driver.quit()

find_elements_list = FindElementsList()
find_elements_list.locate_by_elements_list()