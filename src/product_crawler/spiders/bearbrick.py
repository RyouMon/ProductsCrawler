# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from . import GenericSpider


class BearbrickSpider(GenericSpider):
    name = 'bearbrick'
    allowed_domains = ['bearbrick.com']
    rules = (
        # Match each product in product list.
        Rule(
            LinkExtractor(
                allow=r'.*html',
                restrict_xpaths='//section[@id="itemList"]'
            ), callback='parse'
        ),
        # Match other pages.
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@id="pager"]',
            ),
        )
    )
