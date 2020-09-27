# ProductCrawler
## 介绍
ProductCrawler是一个Scrapy项目，目的是帮助我从购物网站收集商品信息，它包含一系列爬虫，爬虫均以商品的品牌来命名。

我会根据自己和自己团队的需求逐步完善这个项目，如果这能碰巧帮到你那就再好不过了。

目前支持的品牌或购物网站有：
+ [supreme](https://www.supremecommunity.com/)
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

## 开始使用

### 安装Python

我没有将这个项目打包成可执行文件，所以为了使用这个爬虫项目你需要安装Python3。

### 获取项目

右上角有个CODE按钮，直接将整个项目以ZIP的形式下载到你的电脑。

### 安装依赖

解压项目，在项目根目录打开CMD窗口，执行命令：
    
    pip install -r requirements.txt
    
### 爬取

试着执行下面这条命令，项目目录下会创建product目录，所有爬取到的商品图片和信息都会出现在里面。

    python crawl.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/

## 其他依赖

为了使用正确使用nike爬虫，你还需要：
+ Chrome浏览器（chrome version 85）
+ ChromeDriver 85.0.4183.87

缺少它们不会影响其他爬虫的使用。


## 基本使用

命令行执行命令：

    python crawl.py brand start_url...
    
把`brand`替换为品牌名，
把`start_url`替换为要开始爬取的网页，
你需要在项目目录下执行所有的命令。

## 爬虫
### Supreme
爬取某一季所有周的商品  

    python crawl.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplists/

爬取某一周所有的商品  

    python crawl.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/

一次性爬取多个周的商品

    python crawl.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/ https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-05-21/

### Kapital
爬取某一分类下的所有商品

    python crawl.py kapital https://www.kapital-webshop.jp/category/W_COAT/

### Nike
爬取当前搜索款式的商品（包括所有颜色）

    python crawl.py nike https://www.nike.com/cn/w?q=CU6525&vst=CU6525
    
### BearBrick
爬取当前分类的所有商品

    python crawl.py bearbrick http://www.bearbrick.com/product/12_0
    
已知问题：BearBrickLoader的category_in无法达到预期的行为。

### United Arrows Online Shop
爬取当前商品

    python crawl.py uastore https://store.united-arrows.co.jp/shop/mt/goods.html?gid=52711245
    
### Travis Scott
爬取所有商品

    python crawl.py ts https://shop.travisscott.com/ 
