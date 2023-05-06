from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button.click()

    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    browser.execute_script("window.scrollBy(0, 100);")

    x_element = browser.find_element_by_css_selector('#input_value')
    x = int(x_element.text)


    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
