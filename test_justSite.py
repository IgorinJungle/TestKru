import os
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-cache")
# options.add_argument("--height, 800")
# options.add_argument("--width, 600")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 15, poll_frequency=1)


def test_relationships():

# PRECONDITIONS
    driver.get("https://testkru.com/Elements/TextFields")
    driver.maximize_window()
    First_Name = ("xpath", '(//input[@id = "firstName"])[1]')
    Lst_Name = ("xpath", '//input[@id = "lastNameWithPlaceholder"]')
    Text_Area = ("xpath", '//textarea[@class = "pt-1 pb-1 pr-2 pl-2"]')
    Second_First_name = ('xpath', '(//input[@id = "firstName"])[2]')
    Invis_Input = ("xpath", '//input[@id = "invisibleField"]')
    Pre_fieldef_input = ('xpath', '//input[@id = "preFilledTextField"]')


# ACTION
    driver.find_element(*First_Name).send_keys("Igor")
    driver.find_element(*Lst_Name).send_keys("Konovalov")
    driver.find_element(*Text_Area).send_keys("Selenium was here")
    driver.execute_script("window.scrollTo(0,1000)")
    wait.until(EC.visibility_of_element_located(Second_First_name))
    driver.find_element(*Second_First_name).send_keys("Igor, Again")
    driver.find_element(*Pre_fieldef_input).clear()
    time.sleep(5)




