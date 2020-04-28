# -*- coding: utf-8 -*-
from urllib.parse import urlencode

from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ProductCrawler.items import ProductItem
from ProductCrawler.itemloaders import KapitalLoader


class KapitalSpider(CrawlSpider):
    name = 'kapital'
    allowed_domains = ['kapital-webshop.jp']
    rules = [
        Rule(
            LinkExtractor(
                allow=r'.*html',
                restrict_xpaths='//ul[@class="item_list clearfix"]/li//div[@class="img_inner"]/a'
            ),
            callback='parse_item',
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths='//div[@class="pager"]//a'
            ),
            callback='parse',
            follow=True
        )
    ]

    def __init__(self, start_urls, **kwargs):
        super().__init__()
        self.start_urls = start_urls

    def parse_item(self, response):
        loader = KapitalLoader(item=ProductItem(), response=response)
        loader.add_value('brand', 'kapital')
        loader.add_xpath('title', '//h2[@id="itemName"]/text()')
        loader.add_xpath('art_no', '//p[@class="appeal"]/text()')
        loader.add_value('item_url', response.url)
        loader.add_xpath('images', '//div[@class="thumb_list"]//img/@src')
        loader.add_value('image_base_url', 'https://www.kapital-webshop.jp/')
        loader.add_value('category', response.url)
        yield loader.load_item()
