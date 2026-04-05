import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumplayground.practiceprobs.com/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='query']").click()

driver.find_element(By.XPATH, "//input[@name='query']").send_keys("Breed")

results = driver.find_elements(By.XPATH, "//h1[normalize-space()='Akita Inu']")

print(len(results))

time.sleep(5)

for r in results:
    print(r.text)