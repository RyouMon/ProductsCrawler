# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from . import GenericSpider


class NikeSpider(GenericSpider):
    name = 'nike'
    allowed_domains = ['nike.com']
    custom_settings = dict(
            DOWNLOADER_MIDDLEWARES={
                'products_crawler.middlewares.SeleniumDownloaderMiddleware': 543,
            }
    )

    rules = (
        # Match each product in product list.
        Rule(
            LinkExtractor(restrict_xpaths=r'//div[contains(@class, "product-grid__items")]', deny=r'.+jpg'),
            callback='parse',
            follow=True
        ),
        # Match products of other color in product detail.
        Rule(
            LinkExtractor(restrict_xpaths=r'//div[@class="colorway-images-wrapper"]', deny=r'.+jpg'),
            callback='parse',
        )
    )
