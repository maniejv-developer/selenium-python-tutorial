import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class HandleHiddenElements():
    def handle_hidden_elements(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        displayed_1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()

        print(displayed_1)

        time.sleep(2)

        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()

        time.sleep(2)

        displayed_2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()

        print(displayed_2)

        driver.quit()

handle_hidden_elements = HandleHiddenElements()
handle_hidden_elements.handle_hidden_elements()