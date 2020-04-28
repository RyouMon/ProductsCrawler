import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import *


class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst() # 默认使用SelectorList.get()方法


def supreme_week_processor(value):
    match = re.findall(r"\((.*?)\)", value)
    return match[0]


class SupremeLoader(ProductLoader):
    title_out = Compose(
        TakeFirst(),
        lambda x: x.strip(),
        lambda x: x.replace("*", "-"),
        lambda x: x.replace("/", "-"),
    )
    images_out = MapCompose(lambda x: x.replace("thumb", "sqr"))  # 把缩略图的链接替换为源图的链接
    week_out = Compose(TakeFirst(), supreme_week_processor)


class KapitalLoader(ProductLoader):
    art_no_out = Compose(
        TakeFirst(),
        lambda x: x.strip(),
    )
    images_out = Identity()
    category_out = Compose(
        TakeFirst(),
        lambda x: re.findall(r'category/(.*?)/', x),
        lambda x: x[0]
    )


class GallianolandorLoader(ProductLoader):
    price_out = Compose(
        TakeFirst(),
        lambda x: x.strip(),
    )
    images_out = MapCompose(
        lambda x: x.split('?')[0]  # 去除image_url的query部分
    )
    season_out = Compose(
        TakeFirst(),
        lambda x: x.replace('/', '')
    )
