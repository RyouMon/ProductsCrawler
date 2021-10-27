#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from argparse import ArgumentParser
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


parse = ArgumentParser()
parse.add_argument(
    "brand",
    action="store",
    help='指定你要收集的品牌'
)
parse.add_argument(
    "start_urls",
    action="store",
    nargs="+",
    help="指定你要收集商品的所在网址。"
)


def run():
    args = parse.parse_args(sys.argv[1:])
    brand = args.brand
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(brand, **{'start_urls': args.start_urls})
    process.start()


if __name__ == '__main__':
    run()
