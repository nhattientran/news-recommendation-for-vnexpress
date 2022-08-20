import csv
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from crawl_data_vnexpress.items import CrawlLinkItem, CrawlTitle

class CrawlerSpider(Spider):
    name ="news"
    path = 'news/suckhoe.csv'
    allowed_domains = ["vnexpress.net"]
    with open (path) as f:
        reader= csv.DictReader(f)
        Ict = [row for row in reader]
    f.close()
    start_urls = []
    for row in Ict:
        url =row['Url']
        start_urls.append(url)
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.json',
                args={'wait': 2,'html':1},
                dont_filter=True)

    def parse(self, response):
        users = response.xpath('//span[@class="txt-name"]/a/@href').extract()
        title = response.css('title::text').get()
        Abstract = response.xpath('//*[@class="description"]/text()').get()
        NewsID = (response.url).split('-')
        NewsID = NewsID[len(NewsID)-1]
        temp = []
        item = CrawlTitle()
        for user in users:
            if (user is not None) and (user!='javascript:;'):
                user = user.split('/')
                user = user[len(user)-1]
                temp.append(user)
        if temp!=[]:
            item['NewsTitle'] = title
            item['NewsID'] = NewsID.replace('.html','')
            item['NewsAbstract'] = Abstract
            item['UserID'] = " ".join(temp)
            yield item