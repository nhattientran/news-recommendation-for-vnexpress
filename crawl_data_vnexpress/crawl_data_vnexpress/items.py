# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlLinkItem(scrapy.Item):
    Id = scrapy.Field()
    Url = scrapy.Field()

class CrawlTitle(scrapy.Item):
    NewsID = scrapy.Field()
    NewsTitle = scrapy.Field()
    NewsAbstract = scrapy.Field()
    UserID = scrapy.Field()

