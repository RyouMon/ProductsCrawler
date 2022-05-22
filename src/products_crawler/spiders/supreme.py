# -*- coding: utf-8 -*-
from datetime import date
from scrapy import Request
from . import GenericSpider


class SupremeSpider(GenericSpider):
    name = 'supreme'
    allowed_domains = ['supremecommunity.com']
    details_base_url = 'https://www.supremecommunity.com/season/itemdetails/'
    image_base_url = 'https://www.supremecommunity.com'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.start_urls:
            today = date.today()
            season = self.get_season(today.year, today.month)
            self.start_urls = [
                f'https://www.supremecommunity.com/season/{season}/droplist/{d}/'
                for d in self.get_date_formats(today)
            ]

    def parse_start_url(self, response, **kwargs):
        """分析当季的页面，生成每一周的请求对象。
        @url https://www.supremecommunity.com/season/spring-summer2020/droplists/
        @returns requests 21 21
        """
        # 得到每一周的相对地址
        weeks = response.xpath(
            r'//div[@class="catalog-inner"]//a/@href'
        ).getall()
        # 判断该页面是否应该直接交给parse_week()方法进行解析
        if weeks:
            for week in weeks:
                yield Request(self.image_base_url+week, callback=self.parse_week)
        else:
            for request in self.parse_week(response):
                yield request

    def parse_week(self, response):
        """分析每一周的页面，返回对每一个商品的请求。
        @url https://www.supremecommunity.com/season/spring-summer2022/droplist/2022-05-12/
        @returns requests 22 22
        """
        details = response.xpath('//div[@class="catalog-item-top"]/@data-itemid')
        for detail_no in details:
            yield Request(
                url=self.details_base_url+detail_no.get(),
                callback=self.parse,
            )
    
    def parse(self, response, **kwargs):
        """
        @url https://www.supremecommunity.com/season/itemdetails/8911
        @returns items 1 1
        @scrapes brand title item_url images image_base_url season week
        """
        return super().parse(response, **kwargs)

    @staticmethod
    def get_season(year, month):
        return f'spring-summer{year}' if 1 <= month <= 6 else f'fall-winter{year}'

    @staticmethod
    def get_date_formats(today):
        monday = today.day - today.weekday()
        return [f'{today.year}-{today.month}-{day}' for day in range(monday, monday + 7)]
