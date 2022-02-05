from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, Compose

from products_crawler.processors import take_first, take_first_and_strip, identity, \
                                       match_supreme_week, match_kapital_category, \
                                       match_nike_art_no, match_bearbrick_category


class ProductLoader(ItemLoader):
    default_output_processor = take_first
    images_out = identity

    @classmethod
    def delete_url_query_arguments(cls, url):
        return url.rsplit('?', maxsplit=1)[0]


class SupremeLoader(ProductLoader):
    title_out = take_first_and_strip
    images_out = MapCompose(lambda x: x.replace("thumb", "sqr"))
    week_out = Compose(take_first, match_supreme_week)
    season_out = take_first_and_strip


class KapitalLoader(ProductLoader):
    art_no_out = take_first_and_strip
    category_out = Compose(take_first, match_kapital_category)


class GallianolandorLoader(ProductLoader):
    price_out = take_first_and_strip
    images_out = MapCompose(ProductLoader.delete_url_query_arguments)
    season_out = Compose(take_first, lambda x: x.replace('/', ''))


class NikeLoader(ProductLoader):
    images_out = Compose(
        identity,
        lambda urls: [url for url in urls if 'LOADING' not in url]
    )
    art_no_out = Compose(take_first, match_nike_art_no)


class BearBrickLoader(ProductLoader):
    title_out = take_first_and_strip
    category_in = Compose(take_first, match_bearbrick_category)


class UastoreLoader(ProductLoader):
    brand_out = Compose(take_first, lambda x: x.title())


class TsLoader(ProductLoader):
    price_out = take_first_and_strip
    images_out = MapCompose(ProductLoader.delete_url_query_arguments)
