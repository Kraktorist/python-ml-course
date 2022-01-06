#!/usr/bin/env python
import time
from selenium import webdriver
from pathlib import Path

driver_path = Path("/usr/bin/chromedriver")
user_data_dir = Path("/home/kraktorist/.config/chrome")

options = webdriver.ChromeOptions()

# TELL WHERE IS THE DATA DIR
options.add_argument("--user-data-dir={}".format(user_data_dir))

# USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path=driver_path, options=options)

driver.get('https://stepik.org/lesson/568210/step/2?unit=562615')
time.sleep(5)


value = 0.985
while value > 0:
    print(value)
    field = driver.find_element_by_css_selector('input.number-quiz__input')
    field.clear()
    field.send_keys(f"{value}")
    button = driver.find_element_by_css_selector('button.submit-submission')
    button.click()
    time.sleep(3)
    value = value - 0.001