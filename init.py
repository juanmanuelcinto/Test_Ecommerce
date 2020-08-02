import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from categories import CategoriesTest
import csv

class InitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./../chromedriver')

    def test_search(self):
        config_dictionary = {
            "base_url": "",
            "screenshot_width": '768',
            "load_wait": 1,
            "category_test": True,
            'use_auto_height': True
        }

        with open('config.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                value = self.convertValues(row[1])
                config_dictionary[row[0]] = value

        if (config_dictionary["category_test"]):
            CategoriesTest(self.driver, config_dictionary)

    @staticmethod
    def convertValues(value):
        if value == 'false':
            value = False
        elif value == 'true':
            value = True

        return value

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output='reportes', report_name='categories-report'))