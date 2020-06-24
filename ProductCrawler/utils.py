#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.parse import unquote


ILLEGAL_FILENAME_CHARS = {"?", "/", "\\", ":", "*", ">", "<", '"'}


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
    path = ''
    if brand:
        path += brand + '/'
    if season:
        path += season + '/'
    if week:
        path += week + '/'
    elif category:
        path += category + '/'
    if art_no and title:
        item_folder = art_no + '-' + title
    elif art_no and title is None:
        item_folder = art_no
    elif art_no is None and title:
        item_folder = title
    else:
        raise TypeError("At least one of 'title' and 'art_no' must be provided")
    path += legal_name(item_folder) + '/'
    if filename:
        path += filename
    return path


def legal_name(name):
    """
    return a legal file name
    :param name: string
    :return: string
    """
    filename_char_set = set(name)
    illegal_chars = filename_char_set & ILLEGAL_FILENAME_CHARS
    new_name = name
    if illegal_chars:
        for char in illegal_chars:
            new_name = name.replace(char, "_")
    return new_name


def gen_name_from_url(url):
    """
    generate a file name use url
    :param url:
    :return:
    """
    parts = url.split('/')
    if 'nike' in url:
        filename = unquote(parts[-2] + parts[-1])
    else:
        filename = parts[-1]
    return legal_name(filename)


def spider_settings(name):
    """
    get custom spider settings
    :param name: name of spider
    :return: settings -> dict
    """
    settings = dict()
    settings.update(enable_middle_wares(name))
    return settings


def enable_middle_wares(name):
    """
    enable middle wares for spider
    :param name: name of spider
    :return: middle wares setting -> dict
    """
    if name == 'nike':
        return dict(
            DOWNLOADER_MIDDLEWARES={
                'ProductCrawler.middlewares.SeleniumDownloaderMiddleware': 543,
            })
    else:
        return dict()
