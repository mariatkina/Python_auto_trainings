import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#1
def firstFormTry(driver):
    try:
        driver.get("http://suninjuly.github.io/simple_form_find_task.html")
        firstName = driver.find_element(By.CSS_SELECTOR, "input[name='first_name']")
        firstName.send_keys("Ivan")
        lastName = driver.find_element(By.CSS_SELECTOR, "input[name='last_name']")
        lastName.send_keys("Petrov")
        city = driver.find_element(By.XPATH, "//label[.='City:*']/following-sibling::input")
        city.send_keys("Smolensk")
        country = driver.find_element(By.CSS_SELECTOR, "#country")
        country.send_keys("Russia")
        button = driver.find_element(By.CSS_SELECTOR, "#submit_button")
        button.click()

    finally:
        time.sleep(10)
        driver.quit()

def secondTry(driver):
    try:
        driver.get("http://suninjuly.github.io/find_link_text")
        link=driver.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
        link.click()
        firstName = driver.find_element(By.CSS_SELECTOR, "input[name='first_name']")
        firstName.send_keys("Ivan")
        lastName = driver.find_element(By.CSS_SELECTOR, "input[name='last_name']")
        lastName.send_keys("Petrov")
        city = driver.find_element(By.XPATH, "//label[.='City:*']/following-sibling::input")
        city.send_keys("Smolensk")
        country = driver.find_element(By.CSS_SELECTOR, "#country")
        country.send_keys("Russia")
        button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
    finally:
        time.sleep(10)
        driver.quit()

def thirdForm(driver):
    try:
        driver.get("http://suninjuly.github.io/huge_form.html")
        inputFields =driver.find_elements(By.CSS_SELECTOR, "input")
        for field in inputFields:
            field.send_keys("Мой ответ")
        button = driver.find_element(By.CSS_SELECTOR, "button")
        button.click()

    finally:
        time.sleep(10)
        driver.quit()

def fourthForm(driver):
    try:
        driver.get("http://suninjuly.github.io/find_xpath_form")
        firstName = driver.find_element(By.XPATH, "//input[@name='first_name']")
        firstName.send_keys("Ivan")
        lastName = driver.find_element(By.CSS_SELECTOR, "input[name='last_name']")
        lastName.send_keys("Petrov")
        city = driver.find_element(By.XPATH, "//label[.='City:*']/following-sibling::input")
        city.send_keys("Smolensk")
        country = driver.find_element(By.CSS_SELECTOR, "#country")
        country.send_keys("Russia")
        button = driver.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
    finally:
        time.sleep(10)
        driver.quit()

def regForm1(driver, str):
    try:
        driver.get(str)
        firstName=driver.find_element(By.XPATH, "//label[.='First name*']/following-sibling::input")
        firstName.send_keys("Tyusfj")
        lastName=driver.find_element(By.XPATH, "//label[.='Last name*']/following-sibling::input")
        lastName.send_keys("Herr")
        email=driver.find_element(By.CSS_SELECTOR, "input[placeholder*='email'")
        email.send_keys("efskdnv@ndid.ud")
        button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        time.sleep(1)
        wText = driver.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == wText
    finally:
        time.sleep(2)
        driver.quit()

firstFormTry(driver)
secondTry(driver)
thirdForm(driver)
fourthForm(driver)

formLink1 = "http://suninjuly.github.io/registration1.html"
formLink2 = "http://suninjuly.github.io/registration2.html"
regForm1(driver, formLink1)