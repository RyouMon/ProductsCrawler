# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from .generic import GenericSpider


class UastoreSpider(GenericSpider):
    name = 'uastore'
    allowed_domains = ['store.united-arrows.co.jp']

    rules = (
        # matching each item in item list
        Rule(LinkExtractor(restrict_xpaths='//div[@id="itemList"]'), callback='scrap', follow=False),
        # matching other pages
        Rule(LinkExtractor(restrict_xpaths='//div[contains(@id, "pager")]'))
    )

    def parse_start_url(self, response):
        # if response is a item page, parse it use function parse_item.
        if "goods" in response.url:
            return self.parse_item(response)
