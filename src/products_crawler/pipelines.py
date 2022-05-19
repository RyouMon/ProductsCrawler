# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os.path
from os import makedirs
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from products_crawler.settings import IMAGES_STORE
from products_crawler.utils import file_path, gen_name_from_url


class ProductInfoPipeline(object):
    """save item info"""
    def process_item(self, item, spider):
        # 保存路径：
        # images/<brand>/<number>/url.txt
        filepath = file_path(item)
        filepath = os.path.join(IMAGES_STORE, filepath)
        try:
            makedirs(filepath)
        except OSError:
            pass
        with open(os.path.abspath(os.path.join(filepath, 'info.txt')), 'w', encoding='utf-8') as f:
            f.write(str(item.items()))
        return item


class ProductImagesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = gen_name_from_url(request.url)
        file_name = file_path(request.meta['item'], image_name)
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Download Failed')
        return item

    def get_media_requests(self, item, info):
        image_base_url = item.get('image_base_url', None)
        if image_base_url:
            images_url = [image_base_url + part_url for part_url in item['images']]
        else:  # image_base_url is None
            images_url = item['images']
        for image_url in images_url:
            yield Request(image_url, meta={'item': item})
