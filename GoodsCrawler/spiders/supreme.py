# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from GoodsCrawler.itemloaders import SupremeLoader
from GoodsCrawler.items import SupremeItem


class SupremeSpider(CrawlSpider):
    name = 'supreme'
    allowed_domains = ['supremecommunity.com']
    start_urls = ['https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-20/']
    details_base_url = 'https://www.supremecommunity.com/season/itemdetails/'
    image_base_url = 'https://www.supremecommunity.com'
    rules = (
    )

    def parse(self, response):
        details = response.xpath('//div[@class="card-details"]/@data-itemid')
        for detail_no in details:
            yield Request(
                url=self.details_base_url+detail_no.get(),
                callback=self.parse_item
            )

    def parse_item(self, response):
        supreme_loader = SupremeLoader(item=SupremeItem(), response=response)
        supreme_loader.add_value('brand', 'supreme')
        supreme_loader.add_xpath('title', '//h1[@class="detail-title"]/text()')
        supreme_loader.add_value('item_url', response.url)
        supreme_loader.add_xpath('price', '//span[@class="price-label"]/text()')
        supreme_loader.add_value('image_base_url', self.image_base_url)
        supreme_loader.add_xpath('week', '//h2[@class="details-release-small"]/span/text()')
        supreme_loader.load_item()



