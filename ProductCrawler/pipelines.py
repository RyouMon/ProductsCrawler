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

ILLEGAL_FILENAME_CHARS = {"?", "/", "\\", ":", "*", ">", "<", "\""}


class GoodscrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class GoodsUrlPipeline(object):
    """把商品的网址保存为txt文件"""
    def process_item(self, item, spider):
        # 保存路径：
        # images/<brand>/<number>/url.txt
        filepath = file_path(item)
        filepath = IMAGES_STORE + '/' + filepath
        try:
            makedirs(filepath)
        except OSError:
            pass
        filename = filepath + '/url.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(item['item_url'])
        return item


class GoodsImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_name = legal_name(request.url.split('/')[-1])
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
        else: # image_base_url is None
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


def file_path(info, filename=None):
    """
    传入一个包含Item信息的字典，为商品选择一个保存的位置
    :param info: Request.meta or item object.
    :param filename: file name.
    :return: 相对于IMAGE_STORE的路径
    """
    brand = info['brand']
    title = info.get('title')
    art_no = info.get('art_no')
    season = info.get('season')
    week = info.get('week')
    category = info.get('category')
    filepath = ''
    if brand:
        filepath += brand + '/'
    if season:
        filepath += season + '/'
    if week:
        filepath += week + '/'
    elif category:
        filepath += category + '/'
    if art_no:
        filepath += art_no + '/'
    elif title:
        filepath += title + '/'
    else:
        raise TypeError("至少要提供title与art_no的其中一个")
    if filename:
        filepath += filename
    return filepath


def legal_name(filename):
    """
    返回合法的文件名
    :param filename: 可能包含非法字符的文件名字符串。
    :return: 合法的文件名字符串。
    """
    filename_char_set = set(filename)
    illegal_chars = filename_char_set & ILLEGAL_FILENAME_CHARS
    if illegal_chars:
        for char in illegal_chars:
            filename = filename.replace(char, "_")
    return filename
