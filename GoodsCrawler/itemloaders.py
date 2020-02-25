from scrapy.loader import ItemLoader
from scrapy.loader.processors import *


class GoodsLoader(ItemLoader):
    default_output_processor = TakeFirst() # 默认使用SelectorList.get()方法


class SupremeLoader(GoodsLoader):
    title_out = Compose(
        TakeFirst(),
        lambda x: x.replace("*", "-"),
        lambda x: x.replace("/", "-"),
    )
    images_out = MapCompose(lambda x: x.replace("thumb", "sqr"))  # 把缩略图的链接替换为源图的链接
