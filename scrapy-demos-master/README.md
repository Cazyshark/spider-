# scrapy-demos


### 关于

* 这里面的程序是我在学习 Scrapy 时所写的一些例子

* `code is cheap,show me the example`

* 所有的例子都是以 `Xpath` 来作为提取路径，也可以选择`CSS Selector`
---

* 我存储的数据库采用的是 MySQL ,如果要直观运行效果，只需要在`settings.py`中注释掉
`MySQLStorePipeline`即可。用`scrapy crawl spiderName`来执行爬虫，会自动将得到的结果存储在`ans.json`中

* hupu 里是最基本的`Spider`类的使用。抓取了 `虎扑论坛` 上热门点亮回复

* daily_zhihu 和 v2ex 则都是抓取 UGC 内容

* douban 采用了一些 pythonic 的技巧，用`yield`来生成持续的链接。同时添加了`下载图片`的功能。抓取豆瓣书籍数据

* TMT 和 Kr 是`CrawlSpider`类的典型使用。可以在`rules`里看到`follow` 和 `callback`的用法。抓取了 36Kr 和 钛媒体的Top文章

* jd 和 vip 抓取的是京东和唯品会的数据。其中为了测试用，唯品会抓取的是移动版'm.vip.com'。要抓取京东中不同种类的商品数据，需要根据爬虫名来运行不同的爬虫。对于由 AJAX 返回的 JSON 数据，一些可能的解决方法包括：

- [PhantomJs](http://phantomjs.org/)

- [ScrapyJs](https://pypi.python.org/pypi/scrapyjs/0.1.1) (Python Packages)

- 参见 SO 上的[这篇回答](http://stackoverflow.com/questions/8550114/can-scrapy-be-used-to-scrape-dynamic-content-from-websites-that-are-using-ajax)

或者用 requests 来模拟 post 对应接口。参见：[lagou_crawler](https://github.com/Allianzcortex/lagou_crawler)
