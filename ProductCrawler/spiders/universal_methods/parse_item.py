#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ProductCrawler.utils import get_spider_cfg
from ProductCrawler.items import *
from ProductCrawler.itemloaders import *


def parse_item(response, spider):
    spider.logger.info("Parsing Item...")

    # use spider name get config from package: parse_item_cfg.
    cfg = get_spider_cfg(spider.name)['items']

    # initialization Item and ItemLoader.
    item = eval(cfg['class'])()
    loader = eval(cfg['loader'])(item=item, response=response)

    # parse response
    for key, value in cfg['attrs'].items():
        if value["method"] == "":
            continue
        if value["method"] == "value":
            loader.add_value(key, *value["args"])
        elif value["method"] == "xpath":
            loader.add_xpath(key, *value["args"])
        elif value["method"] == "css":
            loader.add_css(key, *value["args"])
        elif value["method"] == "eval":
            loader.add_value(key, *map(eval, value["args"]))
        else:
            raise ValueError("No such method: {0}".format(value["method"]))
    spider.logger.info("Loading Item...")
    return loader.load_item()
