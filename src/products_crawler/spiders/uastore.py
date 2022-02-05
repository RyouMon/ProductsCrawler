# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from . import GenericSpider


class UastoreSpider(GenericSpider):
    name = 'uastore'
    allowed_domains = ['store.united-arrows.co.jp']

    rules = (
        # Match each product in product list.
        Rule(LinkExtractor(restrict_xpaths='//div[@id="itemList"]'), callback='parse'),
        # Match other pages.
        Rule(LinkExtractor(restrict_xpaths='//div[contains(@id, "pager")]'))
    )
