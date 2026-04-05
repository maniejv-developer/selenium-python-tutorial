import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumplayground.practiceprobs.com/dogs/breeds/")

driver.maximize_window()

driver.find_element(By.XPATH, "//label[normalize-space()='Table of Different Dog Breeds']").click()

time.sleep(5)

driver.find_element(By.XPATH, "//th[normalize-space()='Country of Origin']").click()

time.sleep(5)

driver.quit()