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
        dates = [date(2022, 6, 9), date(2022, 5, 1), date(2023, 1, 1)]
        expects = [
            [f'2022-06-{n}' for n in ('06', '07', '08', '09', '10', '11', '12')],
            [f'2022-04-{n}' for n in range(25, 31)] + ['2022-05-01'],
            [f'2022-12-{n}' for n in ('26', '27', '28', '29', '30', '31')] + ['2023-01-01'],
        ]
        for today, expect in zip(dates, expects):
            with self.subTest(today=today):
                self.assertEqual(SupremeSpider.get_date_formats(today), expect)

    def test_init_not_given_start_url_should_generate_7_urls(self):
        spider = SupremeSpider()
        self.assertEqual(len(spider.start_urls), 7)
