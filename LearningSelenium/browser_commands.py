import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class BrowserCommands():
    def browser_commands(self):
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.get("https://the-internet.herokuapp.com")
        time.sleep(2)
        print(driver.current_url)
        time.sleep(2)
        print(driver.title)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "A/B Testing").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(5)
        driver.quit()

browser_commands = BrowserCommands()
browser_commands.browser_commands()