import unittest
from selenium import webdriver
import time

class Test001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\bin\BrowserDriver\chromedriver.exe")
        self.driver.get("https://testeandosoftware.com/blogs-de-testing-en-espanol/")

    def test_001(self):
        boton = self.driver.find_elements_by_xpath('//*[@id="mainnav-menu"]/li[5]')
        time.sleep(5)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()