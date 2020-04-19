from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\bin\BrowserDriver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.cantv.com.ve/")

    def test_001(self):
            #anuncio = self.driver.find_element_by_class_name('fancybox-image')
            anuncio = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div/div/img')
            time.sleep(5)
            anuncio.click()
            time.sleep(5)

    def tearDown(self):
            self.driver.close()

if __name__ == '__main__':
        unittest.main()
