#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
from urllib.parse import unquote
import json


ILLEGAL_FILENAME_CHARS = {"?", "/", "\\", ":", "*", ">", "<", '"', "'"}


def file_path(info, filename=''):
    """
    传入一个包含Item信息的字典，为商品选择一个保存的位置
    :param info: Request.meta or item object.
    :param filename: file name.
    :return: 相对于IMAGE_STORE的路径

    >>> info = {'brand': 'supreme', 'title': 'Boat Tee', 'art_no': '',\
     'season': '20SS', 'week': 'Week18', 'category': '',}

    >>> file_path(info)
    'supreme\\\\20SS\\\\Week18\\\\Boat Tee\\\\'
    >>> file_path(info, 'img.jpg')
    'supreme\\\\20SS\\\\Week18\\\\Boat Tee\\\\img.jpg'
    """
    brand = info.get('brand', '')
    title = info.get('title', '')
    art_no = info.get('art_no', '')
    season = info.get('season', '')
    week = info.get('week', '')
    category = info.get('category', '')
    if art_no and title:
        product = art_no + '-' + legal_name(title)
    elif art_no and not title:
        product = art_no
    elif not art_no and title:
        product = legal_name(title)
    else:
        raise ValueError("At least one of 'title' and 'art_no' must be provided")
    args = [brand, season, week, category, product, filename]
    return os.path.join(*map(legal_name, args))


def legal_name(name):
    """
    return a legal file name
    :param name: string
    :return: string

    >>> legal_name("?, /, \\, :, *, >, <, \'")
    '-, -, -, -, -, -, -, -'
    >>> legal_name('"')
    '-'

    """
    filename_char_set = set(name)
    illegal_chars = filename_char_set & ILLEGAL_FILENAME_CHARS
    for char in illegal_chars:
        name = name.replace(char, "-")
    return name


def gen_name_from_url(url):
    """
    generate a file name use url
    :param url: url without query
    :return: string of filename

    >>> gen_name_from_url('http://www.bearbrick.com/WI/upimage/0122_200724_pfhmgz_b.png')
    '0122_200724_pfhmgz_b.png'

    >>> gen_name_from_url('https://c.imgz.jp/802/53822802/53822802_46_d_500.jpg')
    '53822802_46_d_500.jpg'

    >>> gen_name_from_url('https://c.imgz.jp/802/53822802/53822802_46_d_500.jpg/')
    '53822802_46_d_500.jpg'
    """
    parts = url.split('/')
    if 'nike' in url:
        filename = unquote(parts[-2] + parts[-1])
    elif url.endswith('/'):
        filename = parts[-2]
    else:
        filename = parts[-1]
    return legal_name(filename)


def get_spider_cfg(name):
    """
    get parse item configuration of a specific spider.
    :param name: name of spider
    :return: dictionary of configuration
    """
    with open('products_crawler/spider_configs/{0}.json'.format(name), encoding='utf-8') as f:
        return json.load(f)
