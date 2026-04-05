import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HandleDropdownSingle():
    def handle_dropdown_single(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/dropdown")

        time.sleep(2)

        driver.maximize_window()

        time.sleep(2)

        dropdown = driver.find_element(By.XPATH, "//select[@id='dropdown']")

        single = Select(dropdown)

        single.select_by_index(1)
        time.sleep(2)

        single.select_by_visible_text("Option 2")
        time.sleep(2)

        single.select_by_value("1")
        time.sleep(2)

        driver.quit()

handle_dropdown_single = HandleDropdownSingle()
handle_dropdown_single.handle_dropdown_single()