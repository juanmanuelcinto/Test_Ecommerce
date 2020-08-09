from selenium import webdriver
from time import sleep
import csv

class CategoriesTest:
    def __init__(self, driver, config):
        self._driver = driver
        self._url = config.getValue('base_url')
        self._404_title = config.getValue('404_title')
        self._categories = list(csv.reader(open('categories.csv')))

    def takeScreenshots(self):
        for row in self.categories:
            self._driver.get(self.url + row[1])
            self._driver.set_window_size(self.getWidth() , self.getHeight())
            title = self._driver.title
            if title != self._404_title:
                self._driver.find_element_by_tag_name('body').screenshot('images/' + row[0] + '.png')

    @property
    def url(self):
        return self._url

    @property
    def categories(self):
        return self._categories

    def getHeight(self):
        return self._driver.execute_script('return document.body.scrollHeight')

    def getWidth(self):
        return 1024

    @property
    def driver(self):
        return self._driver