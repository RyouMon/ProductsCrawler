# -*- coding: utf-8 -*-
from urllib.parse import urlencode

from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, Identity
from scrapy.linkextractors import LinkExtractor

from GoodsCrawler.items import KapitalItem


class GoodsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class KapitalLoader(GoodsLoader):
    # 为解决图片保存路径的问题，只能将货号中的'-'符号删除
    no_out = Compose(
        TakeFirst(),
        lambda x: x.strip(),
        lambda x: x.replace('-', '')
    )
    images_out = Identity()


class KapitalSpider(CrawlSpider):
    name = 'kapital'
    allowed_domains = ['kapital-webshop.jp']
    start_urls = []

    rules = (
        Rule(
            LinkExtractor(
                allow=r'.*html',
                restrict_xpaths='//ul[@class="item_list clearfix"]/li//div[@class="img_inner"]/a'
            ),
            callback='parse_item',
            follow=True
        ),
    )

    def start_requests(self):
        base_url = 'https://www.kapital-webshop.jp/category/MENSALL/?'
        query = {
            'SEARCH_MAX_ROW_LIST': 30,
            'item_list_mode': 2,
            'sort_order': 1,
            'request': 'page',
            'next_page': 1
        }
        # 改变Query的next_page参数即可实现横向爬取
        # 其他参数无需变化，参考官网的URL即可。
        for i in range(1, 2):
            query['next_page'] = i
            url = base_url + urlencode(query)
            yield Request(url, self.parse)

    def parse_item(self, response):
        loader = KapitalLoader(item=KapitalItem(), response=response)
        loader.add_value('brand', 'kapital')
        loader.add_xpath('name', '//h2[@id="itemName"]/text()')
        loader.add_xpath('no', '//p[@class="appeal"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('images', '//div[@class="thumb_list"]//img/@src')
        loader.add_value('image_base_url', 'https://www.kapital-webshop.jp/')
        yield loader.load_item()
