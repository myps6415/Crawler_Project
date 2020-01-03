from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class crawler:
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

    def pcstore_crawler(self):
        driver = webdriver.Chrome('/Users/fish/PycharmProjects/pcstore_crawler_selenium/chrome_driver/chromedriver')
        driver.get(self.url)
        time.sleep(3)

        input_bar = driver.find_element_by_id('id_search_word')
        input_bar.send_keys(self.keyword)
        time.sleep(3)

        input_bar.send_keys(Keys.ENTER)
        time.sleep(2)

        return driver.page_source