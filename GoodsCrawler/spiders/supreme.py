# -*- coding: utf-8 -*-
import re
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from GoodsCrawler.itemloaders import SupremeLoader
from GoodsCrawler.items import SupremeItem


class SupremeSpider(CrawlSpider):
    name = 'supreme'
    allowed_domains = ['supremecommunity.com']
    start_urls = ['https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-03-05/']
    details_base_url = 'https://www.supremecommunity.com/season/itemdetails/'
    image_base_url = 'https://www.supremecommunity.com'
    rules = ()
    season = re.findall(r'season/(.*?)/', start_urls[-1]).pop()

    def parse(self, response):
        details = response.xpath('//div[@class="card-details"]/@data-itemid')
        for detail_no in details:
            yield Request(
                url=self.details_base_url+detail_no.get(),
                callback=self.parse_item
            )

    def parse_item(self, response):
        loader = SupremeLoader(item=SupremeItem(), response=response)
        loader.add_value('brand', 'supreme')
        loader.add_xpath('title', '//h1[@class="detail-title"]/text()')
        loader.add_value('item_url', response.url)
        loader.add_xpath('price', '//span[@class="price-label"]/text()')
        loader.add_value('image_base_url', self.image_base_url)
        loader.add_xpath('images', '//div[@class="carousel-inner"]//img/@src')
        loader.add_value('season', self.season)
        loader.add_xpath('week', '//h2[@class="details-release-small"]/span/text()')
        yield loader.load_item()



