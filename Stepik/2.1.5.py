from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = int(x_element.text)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_css_selector("#robotsRule")
    option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
