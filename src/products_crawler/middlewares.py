from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from scrapy.http import HtmlResponse
from logging import getLogger


class SeleniumDownloaderMiddleware(object):
    def __init__(self, timeout=None, chrome_options=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        options = Options()
        for o in chrome_options or ():
            options.add_argument(o)
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.set_window_size(1920, 1080)
        self.browser.set_page_load_timeout(timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.actions = ActionChains(self.browser)

    def __del__(self):
        self.browser.quit()

    def process_request(self, request, spider):
        if request.url.endswith('jpg'):
            return None
        self.logger.debug('Chrome is starting')
        self.browser.get(request.url)
        self.actions.send_keys(Keys.END)
        self.actions.send_keys(Keys.END)
        self.actions.perform()
        time.sleep(1)
        return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, status=200, encoding='utf-8')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
            chrome_options=crawler.settings.get('CHROME_OPTIONS'),
        )
