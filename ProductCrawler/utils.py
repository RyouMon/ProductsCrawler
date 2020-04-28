#!/usr/bin/env python
# -*- coding: utf-8 -*-

ILLEGAL_FILENAME_CHARS = {"?", "/", "\\", ":", "*", ">", "<", "\""}


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
