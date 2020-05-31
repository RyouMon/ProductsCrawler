# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from os import mkdir, makedirs
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from ProductCrawler.settings import IMAGES_STORE
from ProductCrawler.utils import file_path, legal_name


class ProductInfoPipeline(object):
    """save item info"""
    def process_item(self, item, spider):
        # 保存路径：
        # images/<brand>/<number>/url.txt
        filepath = file_path(item)
        filepath = IMAGES_STORE + '/' + filepath
        try:
            makedirs(filepath)
        except OSError:
            pass
        filename = filepath + '/info.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            # f.writelines([k + ': ' + str(v) + '\n' for k, v in item.items()])
            f.write(str(item.items()))
        return item


class ProductImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_name = legal_name(request.url)
        file_name = file_path(request.meta, image_name)
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
            yield Request(image_url,
                          meta={'brand': item.get('brand'),
                                'title': item.get('title'),
                                'art_no': item.get('art_no'),
                                'season': item.get('season'),
                                'week': item.get('week'),
                                'category': item.get('category')}
                          )
