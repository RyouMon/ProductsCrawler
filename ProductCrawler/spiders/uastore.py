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
