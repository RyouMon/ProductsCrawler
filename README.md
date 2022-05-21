# ProductCrawler
[![Version](https://img.shields.io/pypi/v/products_crawler)](https://pypi.org/project/products_crawler/)

## 介绍
ProductCrawler是一个Scrapy项目，目的是从购物网站收集商品信息，它包含一系列爬虫，爬虫均以商品的品牌来命名。

该项目的创建是兴趣使然，目的是学习`Scarpy`框架，可能存在一些Bug和莫名奇妙的代码...

正在生产环境中使用的爬虫有:
+ [supreme](https://www.supremecommunity.com/)

停止维护且不知道能否正常运行的爬虫有:
+ [kapital](https://www.kapital-webshop.jp/)
+ [gallianolandor](https://gallianolandor.com/)
+ [nike](https://www.nike.com/cn/)
+ [bearbrick](http://www.bearbrick.com/product/)
+ [united-arrows online store](https://store.united-arrows.co.jp/)
+ [travis scott](https://shop.travisscott.com/)

正在开发的爬虫有：

等待支持的品牌有：
+ humanmade
+ wtaps

# 依赖
- Python3.7+

- 为了使用 nike 爬虫，你还需要：Chrome 浏览器和相应版本的 ChromeDriver。缺少它们不会影响其他爬虫的使用。

# 安装
```
pip install products_crawler
```

# 用法
```
crawl -h
usage: crawl [-h] {bearbrick,glld,kapital,nike,supreme,ts,uastore} start_urls [start_urls ...]

positional arguments:
  {bearbrick,glld,kapital,nike,supreme,ts,uastore}
  start_urls

optional arguments:
  -h, --help            show this help message and exit
```

试着执行下面这条命令，当前工作目录下会创建product目录，所有爬取到的商品图片和信息都会出现在里面。
```
crawl supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/
```

# 示例
### Supreme
爬取某一季所有周的商品  

    crawl supreme https://www.supremecommunity.com/season/spring-summer2020/droplists/

爬取某一周所有的商品  

    crawl supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/

### Kapital
爬取某一分类下的所有商品

    crawl kapital https://www.kapital-webshop.jp/category/W_COAT/

### Nike
爬取当前搜索款式的商品（包括所有颜色）

    crawl nike https://www.nike.com/cn/w?q=CU6525&vst=CU6525
    
### BearBrick
爬取当前分类的所有商品

    crawl bearbrick http://www.bearbrick.com/product/12_0
    
已知问题：BearBrickLoader的category_in无法达到预期的行为。

### United Arrows Online Shop
爬取当前商品

    crawl uastore https://store.united-arrows.co.jp/shop/mt/goods.html?gid=52711245
    
### Travis Scott
爬取所有商品

    crawl ts https://shop.travisscott.com/ 
