import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HandleAutoSuggestion():
    def handle_auto_suggestion(self):
        driver = webdriver.Chrome()

        time.sleep(2)

        driver.get("https://www.scrapethissite.com/pages/forms/")

        time.sleep(2)

        driver.maximize_window()

        time.sleep(2)

        search = driver.find_element(By.XPATH, "//input[@id='q']")

        time.sleep(2)

        search.click()

        time.sleep(2)

        search.send_keys("New")

        time.sleep(2)

        search.send_keys(Keys.ENTER)

        time.sleep(2)

        results = driver.find_elements(By.CLASS_NAME, "team")

        print(len(results))

        for r in results:
            print(r.text)

handle_auto_suggestion = HandleAutoSuggestion()
handle_auto_suggestion.handle_auto_suggestion()