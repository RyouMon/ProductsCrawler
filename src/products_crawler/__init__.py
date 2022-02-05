import os
from argparse import ArgumentParser

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.spiderloader import SpiderLoader


def main():
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'products_crawler.settings')
    scrapy_settings = get_project_settings()
    spider_loader = SpiderLoader(scrapy_settings)

    parse = ArgumentParser()
    parse.add_argument("brand", choices=spider_loader.list())
    parse.add_argument("start_urls", nargs="+")
    args = parse.parse_args()

    process = CrawlerProcess(scrapy_settings)
    process.crawl(args.brand, **{'start_urls': args.start_urls})
    process.start()


if __name__ == '__main__':
    main()
