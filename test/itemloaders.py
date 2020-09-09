"""
Test Item Loaders
"""
import unittest
from ProductCrawler.itemloaders import *


class ProductLoaderTest(unittest.TestCase):
    def setUp(self):
        self.test_url = 'https://products.com/5S9A1236_1024x1024.jpg?v=1586686713'
        self.loader = ProductLoader()

    def test_should_returnStr(self):
        self.assertEqual(
            self.loader.delete_url_query_arguments(self.test_url),
            'https://products.com/5S9A1236_1024x1024.jpg',
        )


def suite():
    s = unittest.TestSuite()
    load_from = unittest.defaultTestLoader.loadTestsFromTestCase
    s.addTests(load_from(ProductLoaderTest))
    return s


if __name__ == '__main__':
    t = unittest.TextTestRunner()
    t.run(suite())
