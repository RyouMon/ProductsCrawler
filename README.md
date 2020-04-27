# ProductCrawler
## 介绍
ProductCrawler是一个Scrapy项目，目的是帮助电商从业者收集商品信息，它包含一系列爬虫，爬虫均以商品的品牌来命名。

我是一名电商网店的运营者，我相信大家都被“扒图”这个问题困扰过，你也会像曾经的我一样从网站上一张一张保存图片，我通过学习编程来解决了这个问题，这让我从枯燥的重复性动作中解脱了出来。如果你碰巧发现了这个项目你一定会喜欢它。

我会根据自己和自己团队的需求逐步完善这个项目。

目前可以用于简单生产的爬虫有：
+ supreme  
+ kapital
+ gallianolandor

正在开发的爬虫有：

等待添加的爬虫有：
+ bearbrick
+ humanmade
+ wtaps
+ nike

## 安装

克隆仓库到你的电脑：

    $ git clone https://github.com/RyouMon/ProductCrawler/tree/dev

## 依赖

+ Python3.7
+ Scrapy2.0.1
+ pillow7.1.1

## 使用

命令行执行命令：

    $ python3 crawler.py brand start_url

把`brand`替换为品牌名  
把`start_url`替换为要开始爬取的网页

> 这个项目以后会给团队使用，大家都是小白，我也会提供一个从GUI启动爬虫的方式，或许也有更好的方案。
