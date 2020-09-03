# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from .generic import GenericSpider


class BearbrickSpider(GenericSpider):
    name = 'bearbrick'
    allowed_domains = ['bearbrick.com']
    rules = (
        # matching product page, callback with parse_item
        Rule(
            LinkExtractor(
                allow=r'.*html',
                restrict_xpaths='//section[@id="itemList"]'
            ), callback='parse_item', follow=False
        ),
        # matching other pages
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@id="pager"]',
            ),
            follow=True
        )
    )
