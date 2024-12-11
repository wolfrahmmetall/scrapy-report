import scrapy
from scrapy_selenium import SeleniumRequest
import selenium.webdriver as webdriver
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class PipeSpider(scrapy.Spider):
    name = "pipe"
    allowed_domains = ["evraz.market"]
    start_urls = ['https://evraz.market/metalloprokat/listy/list_goryachekatanyy_g_k/']
    
    def start_requests(self):
        url = f"https://evraz.market/metalloprokat/listy/list_goryachekatanyy_g_k/"
        yield SeleniumRequest(url=url, callback=self.parse_page)

    def parse_page(self, response: scrapy.http.Response):
       total_pages = 3 # find total pages number in first page
       for page in range(2, total_pages):
           url = 'https://evraz.market/metalloprokat/listy/list_goryachekatanyy_g_k/' + str(page)  # form page url 
           yield SeleniumRequest(url=url, callback=self.parse)

       yield from self.parse(response)

    def parse(self, response: scrapy.http.Response):
        driver: Chrome = response.request.meta['driver']
        print(driver.current_url)
        for product in driver.find_elements(By.CSS_SELECTOR, '.catalog-item'):
            arm_name = product.find_element(By.CSS_SELECTOR, '.underline-stroke-link').find_element(By.CSS_SELECTOR, 'span').text
            length = product.find_element(By.CSS_SELECTOR, '.main-info__question').text.split(' ')[-1]
            left = product.find_element(By.CSS_SELECTOR, '.catalog-page-stock-status-block').text
            price = [prod.text for prod in product.find_elements(By.CSS_SELECTOR, '.text-nowrap')[:2]]
            yield {
                'name': arm_name,
                'length': length,
                'remaining': left,
                'price range': price,
                'page' : driver.current_url[-1]
            }