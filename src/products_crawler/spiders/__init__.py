import json
from importlib.resources import read_text

from scrapy.spiders import CrawlSpider

from products_crawler import spider_configs
from products_crawler import items, itemloaders


class GenericSpider(CrawlSpider):
    def __init__(self, *args, **kwargs):
        super(GenericSpider, self).__init__()

        self.start_urls = kwargs.pop('start_urls', list())
        self.logger.debug('original start_urls is %r' % self.start_urls)
        if isinstance(self.start_urls, str):
            try:
                self.start_urls = json.loads(self.start_urls)
            except json.JSONDecodeError:
                self.start_urls = [self.start_urls]
        self.logger.debug('cleaned start_urls is %r' % self.start_urls)

        config = self._get_spider_cfg()
        self.item_class = getattr(items, config['item_class'])
        self.loader_class = getattr(itemloaders, config['loader_class'])
        self.load_rules = config.get('load_rules', {})

    def _get_spider_cfg(self):
        content = read_text(spider_configs, f'{self.name}.json')
        return json.loads(content)

    def parse(self, response, **kwargs):
        item = self.item_class()
        loader = self.loader_class(item=item, response=response)

        for field, rule in self.load_rules.items():
            if rule["method"] == "":
                continue
            if rule["method"] == "value":
                loader.add_value(field, *rule["args"])
            elif rule["method"] == "xpath":
                loader.add_xpath(field, *rule["args"])
            elif rule["method"] == "css":
                loader.add_css(field, *rule["args"])
            elif rule["method"] == "eval":
                loader.add_value(field, *map(eval, rule["args"]))
            else:
                raise ValueError("No such method: {0}".format(rule["method"]))

        return loader.load_item()

    def parse_start_url(self, response, **kwargs):
        return self.parse(response)
