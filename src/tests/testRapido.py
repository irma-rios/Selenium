import unittest
from selenium import webdriver
import time

class Test001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\bin\BrowserDriver\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")

    def test_001(self):
        search = self.driver.find_element_by_xpath('//*[@id="search_query_top"]')
        search.send_keys("camisas")
        Presionar = self.driver.find_element_by_xpath('//*[@id="searchbox"]/button').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()