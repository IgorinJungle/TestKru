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
options.add_argument("--headless")
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



def test_Radio_Buttons():
# PRECONDITIONS
    driver.get("https://testkru.com/Elements/RadioButtons")
    driver.maximize_window()
    Single_select_button = ("xpath", '//input[@id = "secondSelect1"]')
    Multi_one = ('xpath', '//input[@id = "firstSelect2"]')
    Multi_two = ("xpath", '//input[@id = "secondSelect2"]')
    Pre_button = ('xpath', '//input[@id = "secondSelect5"]')

# ACTION

    driver.find_element(*Single_select_button).click()

    driver.find_element(*Multi_one).click()
    driver.find_element(*Multi_two).click()
    driver.find_element(*Pre_button).click()



def test_Buttons():
    # PRECONDITIONS
    driver.get("https://testkru.com/Elements/Buttons")
    driver.maximize_window()
    Double_click_Button = driver.find_element("xpath", '//button[@id = "doubleClick"]')
    Right_click_Button = driver.find_element('xpath', '//button[@id = "rightClick"]')
    Left_click_button = driver.find_element("xpath", '//button[@id = "leftClick"]')
    Hover_button = driver.find_element('xpath', '//button[@id = "colorChangeOnHover"]')
    New_tab_button = driver.find_element("xpath", '//button[@id = "openNewTab"]')
    Same_tab_button = driver.find_element("xpath", '//button[@id = "loadNewPageInSameTab"]')


    # ACTION

    action.double_click(Double_click_Button).pause(1)\
    .context_click(Right_click_Button).pause(1)\
    .click(Left_click_button).pause(2)\
    .move_to_element(Hover_button).perform()

    New_tab_button.click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    driver.close()
    tab = driver.window_handles
    driver.switch_to.window(tab[0])
    Same_tab_button.click()


def test_drag_and_drop():
    # PRECONDITIONS
    driver.get("https://testkru.com/Interactions/DragAndDrop")
    driver.maximize_window()
    box1 = driver.find_element('xpath', '(//div[@class = "box"])[1]')
    box2 = driver.find_element('xpath', '(//div[@class = "box"])[2]')
    box3 = driver.find_element('xpath', '(//div[@class = "box"])[3]')
    DropZone1 = driver.find_element('xpath', '//div[@id = "dropZone1"]')
    DropZone2 = driver.find_element("xpath", '//div[@id = "dropZone3"]')

    # ACTION

    action.drag_and_drop(box1, DropZone1).pause(2)\
    .drag_and_drop(box2, DropZone2)\
    .drag_and_drop(box3, DropZone1)\
    .perform()

    time.sleep(5)



def test_frames():
    driver.get("https://testkru.com/Interactions/Frames")

    driver.switch_to.frame("frame2")
    driver.execute_script("window.scrollTo(150,650)")
    driver.switch_to.default_content()
    driver.find_element('xpath', '//a[text() = "codekru"]').click()
    time.sleep(5)
    tab = driver.window_handles
    driver.switch_to.window(tab[1])
    driver.close()
    backtab = driver.window_handles
    driver.switch_to.window(backtab[0])
    time.sleep(3)

