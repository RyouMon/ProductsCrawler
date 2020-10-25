# ProductCrawler
## 介绍
ProductCrawler是一个Scrapy项目，目的是从购物网站收集商品信息，它包含一系列爬虫，爬虫均以商品的品牌来命名。

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

### 安装Python环境

为了使用这个项目你需要Python3的解释环境。

### 获取项目

clone 或者下载这个项目。

### 安装依赖

项目根目录运行命令：
    
    pip install -r requirements.txt
    
### 爬取

试着执行下面这条命令，项目目录下会创建product目录，所有爬取到的商品图片和信息都会出现在里面。

    python crawl.py supreme https://www.supremecommunity.com/season/spring-summer2020/droplist/2020-02-27/

### 其他依赖

为了使用正确使用nike爬虫，你还需要：
+ Chrome浏览器（chrome version 85）
+ ChromeDriver 85.0.4183.87

缺少它们不会影响其他爬虫的使用。

### 配置问题

通过修改`IMAGES_STORE`可以自定义文件的存储位置。

因为项目本身对爬取速度要求不高，
所以默认的`DOWNLOAD_DELAY`为 0.5 ，
如果你需要更快的速度，可以降低这个数值，
为了应对 IP 限制的问题，你可能需要使用代理池。

## 基本使用

项目下执行命令：

    python crawl.py brand start_url...
    
+ 把`brand`替换为品牌名。
+ 把`start_url`替换为要开始爬取的网页。

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
