# ProductCrawler
## 介绍
ProductCrawler是一个Scrapy项目，目的是帮助电商从业者收集商品信息，它包含一系列爬虫，爬虫均以商品的品牌来命名。

我是一名电商网店的运营者，我相信大家都被“扒图”这个问题困扰过，你也会像曾经的我一样从网站上一张一张保存图片，我通过学习编程来解决了这个问题，这让我从枯燥的重复性动作中解脱了出来。如果你碰巧发现了这个项目你一定会喜欢它。

我会根据自己和自己团队的需求逐步完善这个项目。

目前可以用于简单生产的爬虫有：
+ supreme  
+ kapital
+ gallianolandor
+ nike

正在开发的爬虫有：

等待添加的爬虫有：
+ bearbrick
+ humanmade
+ wtaps

## 安装

克隆仓库到你的电脑：

    $ git clone https://github.com/RyouMon/ProductCrawler/tree/dev

## 依赖

该项目主要依赖于
+ python==3.7
+ scrapy==2.0.1
+ pillow==7.1.1

项目中的nike爬虫依赖于以下项
+ selenium==3.141.0
+ chrome version 83
+ ChromeDriver==83.0.4103.39

## 基本使用

命令行执行命令：

    $ python3 crawler.py brand start_url...

把`brand`替换为品牌名  
把`start_url`替换为要开始爬取的网页

## 爬虫
### Supreme
爬取某一季所有的商品  

    $ python3 crawler.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplists/
爬取某一周所有的商品  

    $ python3 crawler.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/

### Kapital
爬取某一分类下的所有商品

    $ python3 crawler.py kapital https://www.kapital-webshop.jp/category/W_COAT/

### Nike
爬取当前搜索款式的商品（包括所有颜色）

    $ python3 crawler.py nike https://www.nike.com/cn/w?q=CU6525&vst=CU6525
    
> 这个项目以后会给团队使用，大家都是小白，我也会提供一个从GUI启动爬虫的方式，或许也有更好的方案。
