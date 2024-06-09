"""
from mathematics import Mathematics

math = Mathematics()
result = math.sumTwoNumbers(10, 20)
print(result)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()
'''
driver.get("https://google.com")
#time.sleep(2)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))
input_element_by_name = driver.find_element(By.NAME, "q")
#input_element_by_class_name = driver.find_element(By.CLASS_NAME, "gLFyf")
#input_element_by_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")

#/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea

#print(input_element_by_name)
#print(input_element_by_class_name)
#print(input_element_by_xpath)

input_element_by_name.send_keys("atil samancioglu")
#time.sleep(2)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "btnK")))


search_button = driver.find_element(By.NAME, "btnK")
#time.sleep(2)
WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "q")))

search_button.click()
'''

driver.get("https://atilsamancioglu.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "button")))
#read_buttons = driver.find_elements(By.CLASS_NAME, "button")

read_button = driver.find_element(By.CLASS_NAME, "button")
read_button.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")))
article_list = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/aside[4]")
print(f"atilsamancioglu.com has {len(article_list.text.splitlines())} blog posts")

while True:
    continue