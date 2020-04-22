# -*- coding: utf-8 -*-
from urllib.parse import urlencode
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from ..items import ProductItem
from ..itemloaders import GallianolandorLoader


class GlldSpider(CrawlSpider):
    name = 'glld'
    allowed_domains = ['gallianolandor.com']
    rules = (
        # 商品区域的所有商品将使用parse_item()方法解析
        Rule(
            LinkExtractor(
                allow=r'.*?products.*?',
                restrict_xpaths=r'//div[@data-section-id="collection-template"]'
            ),
            callback='parse_item',
            follow=True
        ),
    )

    def __init__(self, start_urls, start_page=1, end_page=2):
        super(GlldSpider, self).__init__()
        self.start_urls = start_urls
        self.start_page = start_page
        self.end_page = end_page

    def start_requests(self):
        for start_url in self.start_urls:
            # 商品的横向爬取
            base_url = start_url + "/?"
            query = {
                "page": 1
            }
            for i in range(self.start_page, self.end_page+1):
                query["page"] = i
                url = base_url + urlencode(query)
                yield Request(url, self.parse)

    def parse_item(self, response):
        loader = GallianolandorLoader(item=ProductItem(), response=response)
        loader.add_value('brand', 'GallianoLandor')
        loader.add_xpath(
            'title',
            r'//h1[@class="product-single__title wvendor"]/text()'
        )
        loader.add_value('art_no', None)
        loader.add_value('item_url', response.url)
        loader.add_xpath(
            'images',
            r'//ul[@class="product-single__thumbs grid-uniform"]//a/@href'
        )
        loader.add_xpath(
            'price',
            r'//span[@class="product-price"]/text()'
        )
        loader.add_value('image_base_url', 'https:')
        loader.add_xpath(
            'season',
            r'//a[@class="collection-title text-center"]/text()'
        )
        loader.add_value('week', None)
        loader.add_value('type_', None)
        yield loader.load_item()
