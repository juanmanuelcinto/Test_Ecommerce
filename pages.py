from selenium import webdriver
from time import sleep
import csv

class PagesTest:
    def __init__(self, driver, config):
        self._driver = driver
        self._url = config.getValue('base_url')
        self._404_title = config.getValue('404_title')
        self._pages = list(csv.reader(open('pages.csv')))

    def takeScreenshots(self):
        for row in self.pages:
            self._driver.get(self.url + row[2])
            self._driver.set_window_size(self.getWidth() , self.getHeight())
            title = self._driver.title
            if title != self._404_title:
                self._driver.find_element_by_tag_name('body').screenshot('images/' + row[1] + '-' + row[0] + '.png')

    @property
    def url(self):
        return self._url

    @property
    def pages(self):
        return self._pages

    def getHeight(self):
        return self._driver.execute_script('return document.body.scrollHeight')

    def getWidth(self):
        return 1024

    @property
    def driver(self):
        return self._driver