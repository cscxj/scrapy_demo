from scrapy import Spider

class MySpider(Spider):
    name = 'my_spider'
    start_urls = ["https://www.baidu.com"]