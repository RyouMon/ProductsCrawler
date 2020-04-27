# -*- coding: utf-8 -*-
import re
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ProductCrawler.itemloaders import SupremeLoader
from ProductCrawler.items import ProductItem


class SupremeSpider(CrawlSpider):
    name = 'supreme'
    allowed_domains = ['supremecommunity.com']
    details_base_url = 'https://www.supremecommunity.com/season/itemdetails/'
    image_base_url = 'https://www.supremecommunity.com'

    def __init__(self, start_urls):
        super(SupremeSpider, self).__init__()
        self.start_urls = start_urls
        self.season = re.findall(r'season/(.*?)/', start_urls[-1]).pop()
        self.rules = ()

    def parse_start_url(self, response):
        """
        分析当季的页面，生成每一周的请求对象。
        :param response: 由属性start_urls中url生成的响应对象。
        :return: 每一周的请求对象，回调方法为parse_week()。
        """
        # 得到每一周的相对地址
        weeks = response.xpath(
            r'//div[@class="col-xs-12 col-sm-12 col-md-10 box-list scapp-main-cont"]//a/@href'
        ).getall()
        # 判断该页面是否应该直接交给parse_week()方法进行解析
        if weeks:
            for week in weeks:
                yield Request(
                    url=self.image_base_url+week,
                    callback=self.parse_week
                )
        else:
            yield Request(
                url=response.url,
                callback=self.parse_week
            )

    def parse_week(self, response):
        """
        分析每一周的页面，返回对每一个商品的请求。
        :param response: parse_start_url()方法中返回的请求对象对应的响应对象。
        :return: 对商品的请求对象，回调方法为parse_item()。
        """
        details = response.xpath('//div[@class="card-details"]/@data-itemid')
        for detail_no in details:
            yield Request(
                url=self.details_base_url+detail_no.get(),
                callback=self.parse_item
            )

    def parse_item(self, response):
        loader = SupremeLoader(item=ProductItem(), response=response)
        loader.add_value('brand', 'supreme')
        loader.add_xpath('title', '//h1[@class="detail-title"]/text()')
        loader.add_value('item_url', response.url)
        loader.add_xpath('price', '//span[@class="price-label"]/text()')
        loader.add_value('image_base_url', self.image_base_url)
        loader.add_xpath('images', '//div[@class="carousel-inner"]//img/@src')
        loader.add_value('season', self.season)
        loader.add_xpath('week', '//h2[@class="details-release-small"]/span/text()')
        yield loader.load_item()
