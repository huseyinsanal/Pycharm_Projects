import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestUnicornItems(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))
        username_element = driver.find_element(By.NAME, "username")
        password_element = driver.find_element(By.NAME, "password")

        username_element.send_keys("a")
        password_element.send_keys("b")

        login_element = driver.find_element(By.NAME, "login")
        login_element.click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))
        # /html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul

        alert_message = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")

        assert "ERROR: INCORRECT USERNAME OR PASSWORD" in alert_message.text

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
