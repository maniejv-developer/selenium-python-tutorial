import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class HandleRadioButton():
    def handle_radio_button(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://formy-project.herokuapp.com/radiobutton")

        time.sleep(2)

        driver.maximize_window()

        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='option2']").click()
        selected_1 = driver.find_element(By.XPATH, "//input[@value='option2']").is_selected()
        print(selected_1)

        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='option3']").click()
        selected_2 = driver.find_element(By.XPATH, "//input[@value='option3']").is_selected()
        print(selected_2)

        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='option1']").click()
        selected_3 = driver.find_element(By.XPATH, "//input[@value='option1']").is_selected()
        print(selected_3)

        time.sleep(2)

        driver.quit()

handle_radio_button = HandleRadioButton()
handle_radio_button.handle_radio_button()