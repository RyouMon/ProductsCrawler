import json
from importlib.resources import read_text

from scrapy.spiders import CrawlSpider

from product_crawler import spider_configs
from product_crawler import items, itemloaders


class GenericSpider(CrawlSpider):
    def __init__(self, *args, **kwargs):
        super(GenericSpider, self).__init__()

        # set start_urls
        self.start_urls = kwargs.pop('start_urls', list())
        self.logger.debug('original start_urls is %r' % self.start_urls)
        if isinstance(self.start_urls, str):
            try:
                self.start_urls = json.loads(self.start_urls)
            except json.JSONDecodeError:
                self.start_urls = [self.start_urls]
        self.logger.debug('cleaned start_urls is %r' % self.start_urls)

        # use spider name get config from package: parse_item_cfg.
        self.cfg = self._get_spider_cfg()['items']

        # get Item and ItemLoader class.
        self.item_class = eval('items.' + self.cfg['class'])
        self.loader_class = eval('itemloaders.' + self.cfg['loader'])

    def _get_spider_cfg(self):
        """
        get configuration.
        :return: dictionary of configuration
        """
        content = read_text(spider_configs, f'{self.name}.json')
        return json.loads(content)

    def parse(self, response, **kwargs):
        item = self.item_class()
        loader = self.loader_class(item=item, response=response)

        # parse response
        for key, value in self.cfg['attrs'].items():
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

        return loader.load_item()

    def parse_start_url(self, response, **kwargs):
        return self.parse(response)
