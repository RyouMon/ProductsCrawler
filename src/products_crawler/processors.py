import re

from itemloaders.processors import TakeFirst, Identity, Compose


take_first = TakeFirst()
identity = Identity()
take_first_and_strip = Compose(take_first, lambda x: x.strip())


def match_supreme_week(text):
    return re.findall(r"\((.*?)\)", text)[0]


def match_kapital_category(url):
    return re.findall(r'category/(.*?)/', url)[0]


def match_nike_art_no(text):
    return re.search(r'.{6}-.{3}', text).group()


def match_bearbrick_category(text):
    match = re.search(r'(\d{3}[％%] & )?\d{3,4}[％%]', text)
    if not match:
        return 'other'
    return match.group()
