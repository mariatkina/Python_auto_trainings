import math
import os.path
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

def roboPage(driver):
    try:
        urlpage = "https://suninjuly.github.io/math.html"
        driver.get(urlpage)
        time.sleep(2)
        x_el = driver.find_element(By.CSS_SELECTOR, "span[id='input_value']")
        x = x_el.text
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        y = calc(x)
        answer = driver.find_element(By.CSS_SELECTOR, "#answer")
        answer.send_keys(y)
        chckbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
        rb = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
        chckbox.click()
        rb.click()
        bttn = driver.find_element(By.CSS_SELECTOR, "button")
        bttn.click()

    finally:
        time.sleep(5)
        driver.quit()

# roboPage(driver)

def roboChest(driver):
    try:
        driver.get("http://suninjuly.github.io/get_attribute.html")
        chest = driver.find_element(By.ID, "treasure")
        x = chest.get_attribute("valuex")
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        answer = driver.find_element(By.ID, "answer")
        answer.send_keys(calc(x))
        robotCheckbox = driver.find_element(By.ID, "robotCheckbox")
        robotCheckbox.click()
        robotsRule = driver.find_element(By.ID, "robotsRule")
        robotsRule.click()
        bttn = driver.find_element(By.CSS_SELECTOR, "button")
        bttn.click()

    finally:
        time.sleep(5)
        driver.quit()
# roboChest(driver)
def listSelect1(driver):
    try:
        driver.get("https://suninjuly.github.io/selects1.html")
        x = driver.find_element(By.ID, "num1")
        x = x.text
        y = driver.find_element(By.ID, "num2")
        y = y.text
        def calc(x, y):
            return str(int(x)+int(y))
        selectEl = Select(driver.find_element(By.ID, "dropdown"))
        selectEl.select_by_value(calc(x, y))
        bttn = driver.find_element(By.CSS_SELECTOR, "button")
        bttn.click()

    finally:
        time.sleep(5)
        driver.quit()

# listSelect1(driver)
def useJScript1(driver):
    try:
        driver.get("https://SunInJuly.github.io/execute_script.html")
        x = driver.find_element(By.ID, "input_value")
        x = x.text
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        answer = driver.find_element(By.ID, "answer")
        answer.send_keys(calc(x))
        robotCheckbox = driver.find_element(By.ID, "robotCheckbox")
        robotsRule = driver.find_element(By.ID, "robotsRule")
        bttn = driver.find_element(By.CSS_SELECTOR, "button")
        driver.execute_script("return arguments[0].scrollIntoView(true)", bttn)
        robotCheckbox.click()
        robotsRule.click()
        bttn.click()

    finally:
        time.sleep(5)
        driver.quit()
# useJScript1(driver)

def addFileToForm(driver):
    try:
        driver.get("http://suninjuly.github.io/file_input.html")
        firstname = driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
        lastname = driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
        email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
        addFileBttn = driver.find_element(By.ID, "file")
        file_path = "C:/Users/1/Desktop/"
        file_name = "текст.txt"
        file = os.path.join(file_path, file_name)
        firstname.send_keys("Tokldjufh")
        lastname.send_keys("Fwyeg")
        email.send_keys("adih@uh.ty")
        addFileBttn.send_keys(file)
        bttn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        bttn.click()

    finally:
        time.sleep(5)
        driver.quit()

# addFileToForm(driver)
def workWithAlerts(driver):
    try:
        driver.get("http://suninjuly.github.io/alert_accept.html")
        bttn = driver.find_element(By.TAG_NAME, "button")
        bttn.click()
        confirm = driver.switch_to.alert
        confirm.accept()
        x = driver.find_element(By.ID, "input_value")
        x = x.text
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        ans = driver.find_element(By.ID, "answer")
        ans.send_keys(calc(x))
        submitBttn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submitBttn.click()

    finally:
        time.sleep(5)
        driver.quit()

# workWithAlerts(driver)

def workWithWindws(driver):
    try:
        driver.get("http://suninjuly.github.io/redirect_accept.html")
        bttn = driver.find_element(By.TAG_NAME, "button")
        bttn.click()
        new_wndw = driver.window_handles[1]
        driver.switch_to.window(new_wndw)
        x = driver.find_element(By.ID, "input_value")
        x = x.text
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        ans = driver.find_element(By.ID, "answer")
        ans.send_keys(calc(x))
        submitBttn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submitBttn.click()

    finally:
        time.sleep(5)
        driver.quit()

# workWithWindws(driver)


def expectForBooking(driver):
    try:
        driver.get("http://suninjuly.github.io/explicit_wait2.html")
        bttn = driver.find_element(By.ID, "book")
        price = driver.find_element(By.ID, "price")
        WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
        bttn.click()
        driver.execute_script("window.scrollBy(0, 150)")
        x = driver.find_element(By.ID, "input_value")
        x = x.text
        def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))
        ans = driver.find_element(By.ID, "answer")
        ans.send_keys(calc(x))
        submitBttn = driver.find_element(By.ID, "solve")
        submitBttn.click()

    finally:
        time.sleep(5)
        driver.quit()

# expectForBooking(driver)