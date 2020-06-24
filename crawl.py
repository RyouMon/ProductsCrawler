#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ProductCrawler.arg_parser import parse


def run():
    name_space = parse.parse_args(sys.argv[1:])
    brand = name_space.brand
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(brand, **{'start_urls': name_space.start_urls})
    process.start()


if __name__ == '__main__':
    run()
