import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GetElementAttribute():
    def locate_by_element_attribute(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://the-internet.herokuapp.com/upload")

        time.sleep(2)

        value = driver.find_element(By.XPATH, "//input[@id='file-submit']").get_attribute("value")

        print(value)

        time.sleep(2)

        driver.quit()

get_element_attribute = GetElementAttribute()
get_element_attribute.locate_by_element_attribute()