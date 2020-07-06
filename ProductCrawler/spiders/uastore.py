# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ProductCrawler.spiders.universal_methods.parse_item import parse_item


class UastoreSpider(CrawlSpider):
    name = 'uastore'
    allowed_domains = ['store.united-arrows.co.jp']

    rules = (
        # matching each item in item list
        Rule(LinkExtractor(restrict_xpaths='//div[@id="itemList"]'), callback='scrap', follow=False),
        # matching other pages
        Rule(LinkExtractor(restrict_xpaths='//div[contains(@id, "pager")]'))
    )

    def __init__(self, start_urls=None):
        super(UastoreSpider, self).__init__()
        if start_urls:
            self.start_urls = start_urls

    def parse_start_url(self, response):
        # if response is a item page, parse it use function parse_item.
        if "goods" in response.url:
            return parse_item(response, self)

    def call_parse_item(self, response):
        # parse response use function parse_item
        return parse_item(response, self)