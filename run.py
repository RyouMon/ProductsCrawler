#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run():
    name = sys.argv[1]
    project_settings = get_project_settings()
    process = CrawlerProcess(project_settings)

    process.crawl(name, **{'start_urls': sys.argv[2:]})
    process.start()


if __name__ == '__main__':
    run()
