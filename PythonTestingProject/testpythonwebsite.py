import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_something(self):
        driver = self.driver
        driver.get("https://pypi.org/")
        print(driver.title)

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
