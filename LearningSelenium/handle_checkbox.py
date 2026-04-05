import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class HandleCheckbox():
    def handle_checkbox(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/checkboxes")

        time.sleep(2)

        driver.maximize_window()

        time.sleep(2)

        driver.find_element(By.XPATH, "//input[1]").click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//input[2]").click()

        time.sleep(2)

        driver.quit()

handle_checkbox = HandleCheckbox()
handle_checkbox.handle_checkbox()