import scrapy
from scrapy_selenium import SeleniumRequest
import selenium.webdriver as webdriver
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By




class RailsSpider(scrapy.Spider):
    name = "angles"
    allowed_domains = ["evraz.market"]
    start_urls = ["https://evraz.market/metalloprokat/fasonnyy_prokat/ugolok/"]

    def start_requests(self):
        url = "https://evraz.market/metalloprokat/fasonnyy_prokat/ugolok/"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        driver: Chrome = response.request.meta['driver']
        
        for product in driver.find_elements(By.CSS_SELECTOR, '.catalog-item'):
            arm_name = product.find_element(By.CSS_SELECTOR, 'span.underline-stroke-link').find_element(By.CSS_SELECTOR, 'span').text
            length = product.find_element(By.CSS_SELECTOR, '.main-info__question').text.split(' ')[-1]
            left = product.find_element(By.CSS_SELECTOR, '.catalog-page-stock-status-block').text
            price = [prod.text for prod in product.find_elements(By.CSS_SELECTOR, '.text-nowrap')[:2]]
            yield {
                'name': arm_name,
                'length': length,
                'remaining': left,
                'price range': price
            }
