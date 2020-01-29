# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import urlencode
from GoodsCrawler.items import KapitalItem


class KapitalSpider(Spider):
    """
    爬取Kapital品牌的商品。
    该爬虫的目的是测试爬取规则，经过调整也可以用于生产。
    """
    name = 'kapital'
    allowed_domains = ['kapital-webshop.jp']
    start_urls = ['']

    def start_requests(self):
        base_url = 'https://www.kapital-webshop.jp/category/MENSALL/?'
        query = {
            'SEARCH_MAX_ROW_LIST': 30,
            'item_list_mode': 2,
            'sort_order': 1,
            'request': 'page',
            'next_page': 1
        }
        for i in range(1, 2):
            query['next_page'] = i
            url = base_url + urlencode(query)
            yield Request(url, self.parse)

    def parse(self, response):
        error = response.xpath('//div[@id="error"]')
        # 检查获取的是否为正确的页面
        if not error:
            items = response.xpath('//ul[@class="item_list clearfix"]/li')
            for item in items:
                item_url = item.xpath('.//div[@class="img_inner"]/a/@href').get()
                yield Request(item_url, self.parse_item)
        else:
            pass

    def parse_item(self, response):
        item = KapitalItem()
        item['brand'] = 'kapital'
        item['item_name'] = response.xpath('//h2[@id="itemName"]/text()').get()
        item['item_no'] = response.xpath('//p[@class="appeal"]/text()').get().strip().replace('-', '')
        item['item_url'] = response.url
        item['images'] = response.xpath('//div[@class="thumb_list"]//img/@src').getall()
        yield item
