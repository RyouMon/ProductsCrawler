import json
from scrapy.spiders import CrawlSpider
from ProductCrawler import items, itemloaders


class GenericSpider(CrawlSpider):
    def __init__(self, *args, **kwargs):
        super(GenericSpider, self).__init__()
        self.start_urls = kwargs.pop('start_urls', list())
        if isinstance(self.start_urls, str):
            self.start_urls = [self.start_urls]
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
        with open('ProductCrawler/spider_configs/{0}.json'.format(self.name), encoding='utf-8') as f:
            return json.load(f)

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
