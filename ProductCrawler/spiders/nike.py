# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from .generic import GenericSpider


class NikeSpider(GenericSpider):
    name = 'nike'
    allowed_domains = ['nike.com']
    custom_settings = dict(
            DOWNLOADER_MIDDLEWARES={
                'ProductCrawler.middlewares.SeleniumDownloaderMiddleware': 543,
            }
    )

    rules = (
        # Match each product in search list
        Rule(
            LinkExtractor(restrict_xpaths=r'//div[contains(@class, "product-grid__items")]', deny=r'.+jpg'),
            callback='parse_item',
            follow=True
        ),
        # Matching products of other color in product detail
        Rule(
            LinkExtractor(restrict_xpaths=r'//div[@class="colorway-images-wrapper"]', deny=r'.+jpg'),
            callback='parse_item',
            follow=False
        )
    )
