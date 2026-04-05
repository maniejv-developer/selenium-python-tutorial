import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HandleDropdownMultiple():
    def handle_dropdown_multiple(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://demoqa.com/select-menu")

        time.sleep(2)

        driver.maximize_window()

        time.sleep(2)

        dropdown = driver.find_element(By.ID, "cars")

        multiple = Select(dropdown)

        multiple.select_by_index(0)
        time.sleep(2)

        multiple.select_by_value("saab")
        time.sleep(2)

        multiple.select_by_visible_text("Audi")
        time.sleep(2)

        multiple.deselect_by_index(0)
        time.sleep(2)

        multiple.deselect_all()
        time.sleep(2)

        driver.quit()

handle_dropdown_multiple = HandleDropdownMultiple()
handle_dropdown_multiple.handle_dropdown_multiple()