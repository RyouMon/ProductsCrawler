from unittest import TestCase
from datetime import date

from products_crawler.spiders.supreme import SupremeSpider


class SupremeSpiderTest(TestCase):

    def test_get_season_given_jan_should_return_summer(self):
        self.assertEqual(SupremeSpider.get_season(2022, 1), 'spring-summer2022')

    def test_get_season_given_jun_should_return_summer(self):
        self.assertEqual(SupremeSpider.get_season(2022, 6), 'spring-summer2022')

    def test_get_season_given_jul_should_return_winter(self):
        self.assertEqual(SupremeSpider.get_season(2022, 7), 'fall-winter2022')

    def test_get_season_given_dec_should_return_winter(self):
        self.assertEqual(SupremeSpider.get_season(2022, 12), 'fall-winter2022')

    def test_get_date_formats_should_return_list_contains_10_str(self):
        today = date(2022, 5, 21)
        expects = [f'2022-5-{n}' for n in range(16, 23)]
        self.assertListEqual(SupremeSpider.get_date_formats(today), expects)

    def test_init_not_given_start_url_should_generate_7_urls(self):
        spider = SupremeSpider()
        self.assertEqual(len(spider.start_urls), 7)
