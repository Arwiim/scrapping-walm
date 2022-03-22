import scrapy
import json
from scrapy.crawler import CrawlerProcess

class Forever21Spider(scrapy.Spider):
    
    name = 'forever21'
    
    payload = {'sl': '63c6cac5-a4b5-4191-a52a-65582db8f8b3',
              'PS': 48, 'cc': 50, 'PageNumber': 1, 0: 'OrderByReviewRateDESC',
              'sm': 0, 'fq': 'C:/1/', 'sc': 15}
    
    #url = 'https://www.walmart.com.ar/buscapagina?sl=63c6cac5-a4b5-4191-a52a-65582db8f8b3&PS=48&cc=50&PageNumber=2&O=OrderByReviewRateDESC&sm=0&fq=C:/1/&sc=15'
    url = "https://www.walmart.com.ar/"
    
    def start_requests(self):
        # scrape the first page
        payload = self.payload.copy()
        payload['PageNumber'] = 1
        scrapy.Request(
            self.url, method='POST',
            headers={'X-Requested-With': 'XMLHttpRequest',
                     'Content-Type': 'application/json; charset=UTF-8'},
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.text)
        print(data)
