import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class CheckElementEnabled():
    def check_element_enabled(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/dynamic_controls")

        time.sleep(2)

        is_enabled_1 = driver.find_element(By.XPATH, "//input[@type='text']").is_enabled()

        print(is_enabled_1)

        driver.find_element(By.XPATH, "//button[normalize-space()='Enable']").click()

        time.sleep(10)

        is_enabled_2 = driver.find_element(By.XPATH, "//input[@type='text']").is_enabled()

        print(is_enabled_2)

        time.sleep(2)

        driver.quit()

check_if_element_enabled = CheckElementEnabled()
check_if_element_enabled.check_element_enabled()