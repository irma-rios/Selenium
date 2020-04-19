from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Test_001(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.3\bin\BrowserDriver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://testeandosoftware.com/blogs-de-testing-en-espanol/")

    def test_001(self):
            time.sleep(2.5)
            buscar = self.driver.find_element_by_class_name("search-field")
            buscar.click()
            time.sleep(2.5)
            buscar.send_keys("testing manual")
            time.sleep(2.5)
            buscar.send_keys(Keys.ENTER)
            time.sleep(2.5)
            buscar = self.driver.find_element_by_class_name("search-field")
            buscar.click()
            buscar.clear()
            time.sleep(2.5)
            self.driver.refresh()
            time.sleep(2.5)
            accion = ActionChains(self.driver)
            formacion = self.driver.find_element_by_xpath('//*[@id="mainnav-menu"]/li[2]')
            accion.move_to_element(formacion).perform()
            presentacion = self.driver.find_element_by_xpath("//*[contains(text(), 'Presentaciones')]")
            accion.move_to_element(presentacion).perform()
            presentacion.click()
            time.sleep(2.5)

    def tearDown(self):
            assert "Presentación Archives - Testeando Software" in self.driver.title
            self.driver.close()

if __name__ == '__main__':
        unittest.main()