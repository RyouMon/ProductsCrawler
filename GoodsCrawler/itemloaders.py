from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, Identity


class GoodsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class SupremeLoader(GoodsLoader):
    pass