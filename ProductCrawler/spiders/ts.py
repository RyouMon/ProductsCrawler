# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from .generic import GenericSpider


class TsSpider(GenericSpider):
    name = 'ts'
    allowed_domains = ['travisscott.com']
    rules = (
        # matching each item in item list
        Rule(LinkExtractor(allow=r'.*products.*'), callback='parse_item', follow=True),
    )
