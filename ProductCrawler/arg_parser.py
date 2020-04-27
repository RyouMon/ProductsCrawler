#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser


parse = ArgumentParser(description="我是ProductCrawler，我会帮助你收集商品的信息。")
# 参数：品牌（必选）
parse.add_argument(
    "brand",
    action="store",
    help='指定你要收集的品牌'
)
# 参数：开始爬取的网络地址（至少为一个）
parse.add_argument(
    "start_urls",
    action="store",
    nargs="+",
    help="指定你要收集商品的所在网址。"
)


if __name__ == '__main__':
    import sys
    print(sys.argv)
    namespace = parse.parse_args(sys.argv[1:])
    print(namespace)
