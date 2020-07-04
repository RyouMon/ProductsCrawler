# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ProductCrawler.spiders.universal_methods.parse_item import parse_item


class BearbrickSpider(CrawlSpider):
    name = 'bearbrick'
    allowed_domains = ['bearbrick.com']
    rules = (
        # matching product page, callback with parse_item
        Rule(
            LinkExtractor(
                allow=r'.*html',
                restrict_xpaths='//section[@id="itemList"]'
            ), callback='call_parse_item', follow=False
        ),
        # matching other pages
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@id="pager"]',
            ),
            follow=True
        )
    )

    def __init__(self, start_urls=None):
        super(BearbrickSpider, self).__init__()
        self.parse_item = parse_item
        if start_urls:
            self.start_urls = start_urls

    def call_parse_item(self, response):
        return parse_item(response, self)
