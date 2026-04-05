from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumplayground.practiceprobs.com/")

title = driver.find_element(By.ID, "selenium-playground")

print(title.text)

driver.quit()