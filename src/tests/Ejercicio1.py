from selenium import webdriver
import unittest
import time

class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\bin\BrowserDriver\chromedriver.exe")
        self.driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    def test_001(self):
        driver = self.driver
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()