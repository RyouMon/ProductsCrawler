# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class GoodsItem(Item):
    brand = Field()
    title = Field()
    art_no = Field()
    item_url = Field()
    images = Field()
    price = Field()
    image_base_url = Field()
    season = Field()
    week = Field()
    type_ = Field()


class KapitalItem(GoodsItem):
    image_base_url = Field()


class SupremeItem(GoodsItem):
    image_base_url = Field()
    season = Field()
    week = Field()
    type_ = Field()
