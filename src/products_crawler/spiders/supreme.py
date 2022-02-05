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
            year, week, _ = today.isocalendar()
            month = today.month
            season = f'spring-summer{year}' if 1 <= month <= 6 else f'fall-winter{year}'
            for day in range(1, 8):
                date_ = date.fromisocalendar(year, week, day)
                url = f'https://www.supremecommunity.com/season/{season}/droplist/{date_.isoformat()}/'
                self.start_urls.append(url)

    def parse_start_url(self, response, **kwargs):
        """
        分析当季的页面，生成每一周的请求对象。
        :param response: 由属性start_urls中url生成的响应对象。
        :return: 每一周的请求对象，回调方法为parse_week()。
        """
        # 得到每一周的相对地址
        weeks = response.xpath(
            r'//div[@class="catalog-inner"]//a/@href'
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
        details = response.xpath('//div[@class="catalog-item-top"]/@data-itemid')
        for detail_no in details:
            yield Request(
                url=self.details_base_url+detail_no.get(),
                callback=self.parse,
            )
