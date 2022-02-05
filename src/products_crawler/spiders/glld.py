# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from . import GenericSpider


class GlldSpider(GenericSpider):
    name = 'glld'
    allowed_domains = ['gallianolandor.com']
    rules = (
        # Match each item in item list.
        Rule(
            LinkExtractor(
                allow=r'.*?products.*?',
                restrict_xpaths=r'//div[@data-section-id="collection-template"]'
            ),
            callback='parse',
        ),
        # Match other pages.
        Rule(
            LinkExtractor(
                restrict_xpaths=r'//ul[@class="pagination-custom"]'
            )
        )
    )
