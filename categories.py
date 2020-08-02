from selenium import webdriver
import csv
from time import sleep

class CategoriesTest(object):
    def __init__(self, driver, config):
        self._driver = driver
        base_url = config['base_url']
        self._url = base_url
        window_width = config['screenshot_width']

        with open('categories.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                driver.get(base_url + row[1])
                sleep(int(config['load_wait']))
                if config['use_auto_height']:
                    window_height = driver.execute_script('return document.body.scrollHeight')
                else:
                    window_height = row[2]
                driver.set_window_size(window_width , window_height)                                                                                                                
                driver.find_element_by_tag_name('body').screenshot('images/' + row[0] + '.png')