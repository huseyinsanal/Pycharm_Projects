"""
from mathematics import Mathematics

math = Mathematics()
result = math.sumTwoNumbers(10, 20)
print(result)
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")
input_element_by_name = driver.find_element(By.NAME, "q")
#input_element_by_class_name = driver.find_element(By.CLASS_NAME, "gLFyf")
#input_element_by_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")

#/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea

print(input_element_by_name)
#print(input_element_by_class_name)
#print(input_element_by_xpath)

while True:
    continue