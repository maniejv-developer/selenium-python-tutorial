import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

class FindElementId():
    def locate_by_id(self):
        chrome_options = Options()

        if os.getenv('JENKINS_URL'):
            print("🚀 Detected Jenkins - Connecting to Remote Grid...")
            chrome_options.add_argument("--headless")
            grid_url = os.getenv('SELENIUM_GRID_URL', 'http://selenium-chrome:4444')
            driver = webdriver.Remote(command_executor=grid_url, options=chrome_options)
        else:
            print("💻 Detected MacBook - Running Locally...")
            driver = webdriver.Chrome(options=chrome_options)

        time.sleep(5)

        driver.get("https://the-internet.herokuapp.com/login")

        time.sleep(5)

        driver.find_element(By.ID, "username").send_keys("tomsmith")

        time.sleep(5)

        driver.quit()

find_element_id = FindElementId()
find_element_id.locate_by_id()