import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class FindElementId():
    def locate_by_id(self):
        chrome_options = Options()

        chrome_options.add_argument("--headless")

        driver = webdriver.Remote(
            command_executor='http://selenium-standalone:4444/wd/hub',
            options=chrome_options
        )

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.ID, "username").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_id = FindElementId()
find_element_id.locate_by_id()