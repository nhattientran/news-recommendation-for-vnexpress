import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawl_data_vnexpress.items import CrawlLinkItem

class CrawlerSpider(Spider):
    name = "links"
    allowed_domains = ["vnexpress.net"]
    def start_requests(self):
        limit = int(self.limit)
        for i in range(limit):
            p = i+1
            yield scrapy.Request(f'https://vnexpress.net/{self.topic}-p{p}')

    def parse(self, response):

        links = response.xpath('//h3/a/@href').extract()
        if links==[]:
            links = response.xpath('//h2/a/@href').extract()
        for Url in links:
            item = CrawlLinkItem()
            Id = Url.split('-')
            Id = Id[len(Id)-1]
            Id = Id.replace('.html','')
            item['Url'] = Url
            item['Id'] = Id
            yield item
