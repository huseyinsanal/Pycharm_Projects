import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPythonWebsite(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://pypi.org/")
        #print(driver.page_source)
        self.assertIn("PyPI", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        assert "There were no results for" in driver.page_source

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
