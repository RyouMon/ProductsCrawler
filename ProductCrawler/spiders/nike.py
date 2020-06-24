# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ProductCrawler.items import ProductItem
from ProductCrawler.itemloaders import NikeLoader


class NikeSpider(CrawlSpider):
    name = 'nike'
    allowed_domains = ['nike.com']
    custom_settings = dict(
            DOWNLOADER_MIDDLEWARES={
                'ProductCrawler.middlewares.SeleniumDownloaderMiddleware': 543,
            }
    )

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=r'//div[contains(@class, "product-grid__items")]', deny=r'.+jpg'),
            callback='parse_item',
            follow=True
        ),
        Rule(
            LinkExtractor(restrict_xpaths=r'//div[@class="colorway-images-wrapper"]', deny=r'.+jpg'),
            callback='parse_item',
            follow=False
        )

    )

    def __init__(self, start_urls):
        super(NikeSpider, self).__init__()
        self.start_urls = start_urls

    def parse_item(self, response):
        loader = NikeLoader(item=ProductItem(), response=response)
        loader.add_value('brand', 'Nike')
        loader.add_value('title', self.parse_title(response))
        loader.add_xpath('art_no', '//li[@class="description-preview__style-color ncss-li"]/text()')
        loader.add_value('item_url', response.url)
        loader.add_xpath('price', '//div[@class="css-b9fpep"]/text()')
        loader.add_xpath('images', '//div[@id="pdp-6-up"]//img/@src')
        loader.add_value('season', None)
        loader.add_xpath('week', None)
        yield loader.load_item()

    @staticmethod
    def parse_title(response):
        h1 = response.xpath(r'//h1[@id="pdp_product_title"]/text()').get()
        h2 = response.xpath(r'//h2[@class="headline-5-small pb1-sm d-sm-ib css-6yhqc5"]/text()').get()
        return h1 + ' ' + h2
