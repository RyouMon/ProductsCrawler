# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from os import mkdir, makedirs
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class GoodscrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class GoodsUrlPipeline(object):
    """把商品的网址保存为txt文件"""
    def process_item(self, item, spider):
        # 保存路径：
        # images/<brand>/<number>/url.txt
        filepath = 'images/' + item['brand'] + '/' + item['no']
        try:
            makedirs(filepath)
        except OSError:
            pass
        filename =  filepath + '/url.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(item['url'])
        return item


class KapitalImagesPipeline(ImagesPipeline):
    """把Kapital的图片下载到image文件夹下"""
    image_base_url = 'https://www.kapital-webshop.jp/'

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_path = url.split('/')[-2]
        file_name = 'kapital/' + file_path + '/' + url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Download Failed')
        return item

    def get_media_requests(self, item, info):
        for part_url in item['images']:
            yield Request(KapitalImagesPipeline.image_base_url+part_url)
