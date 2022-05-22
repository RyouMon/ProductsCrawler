# -*- coding: utf-8 -*-

BOT_NAME = 'products_crawler'

SPIDER_MODULES = ['products_crawler.spiders']
NEWSPIDER_MODULE = 'products_crawler.spiders'

FILES_STORE = r'products'

SELENIUM_TIMEOUT = 20
CHROME_OPTIONS = ['--headless']

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 0.1

TELNETCONSOLE_ENABLED = False

ITEM_PIPELINES = {
    'products_crawler.pipelines.ProductInfoPipeline': 300,
    'products_crawler.pipelines.ProductImagesPipeline': 301,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.2
AUTOTHROTTLE_MAX_DELAY = 0.5
AUTOTHROTTLE_TARGET_CONCURRENCY = 3.0
