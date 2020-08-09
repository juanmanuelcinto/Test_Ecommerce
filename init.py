import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from config import Config
from pages import PagesTest

class InitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./../chromedriver')

    def test_pages(self):
        config = Config('config.csv')
        pages = PagesTest(self.driver, config)

        pages.takeScreenshots()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output='reportes', report_name='jmc-report'))