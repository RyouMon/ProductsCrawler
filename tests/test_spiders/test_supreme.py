from unittest import TestCase
from products_crawler.spiders.supreme import SupremeSpider


class SupremeTest(TestCase):

    def test_get_season_given_jan_should_return_summer(self):
        self.assertEqual(SupremeSpider.get_season(2022, 1), 'spring-summer2022')

    def test_get_season_given_jun_should_return_summer(self):
        self.assertEqual(SupremeSpider.get_season(2022, 6), 'spring-summer2022')

    def test_get_season_given_jul_should_return_winter(self):
        self.assertEqual(SupremeSpider.get_season(2022, 7), 'fall-winter2022')

    def test_get_season_given_dec_should_return_winter(self):
        self.assertEqual(SupremeSpider.get_season(2022, 12), 'fall-winter2022')
