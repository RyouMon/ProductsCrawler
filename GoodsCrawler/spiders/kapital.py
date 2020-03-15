# -*- coding: utf-8 -*-
from urllib.parse import urlencode

from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from GoodsCrawler.items import KapitalItem
from GoodsCrawler.itemloaders import KapitalLoader


class KapitalSpider(CrawlSpider):
    name = 'kapital'
    allowed_domains = ['kapital-webshop.jp']
    start_urls = []

    # 动态构建Rule对象可以实现特定商品的爬取。
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
        loader.add_xpath('title', '//h2[@id="itemName"]/text()')
        loader.add_xpath('art_no', '//p[@class="appeal"]/text()')
        loader.add_value('item_url', response.url)
        loader.add_xpath('images', '//div[@class="thumb_list"]//img/@src')
        loader.add_value('image_base_url', 'https://www.kapital-webshop.jp/')
        yield loader.load_item()
