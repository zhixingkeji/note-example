import scrapy


class JobtextSpider(scrapy.Spider):
    name = 'jobtext'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
