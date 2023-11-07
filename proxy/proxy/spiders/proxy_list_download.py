import scrapy


class ProxyListDownloadSpider(scrapy.Spider):
    name = "proxy-list.download"
    allowed_domains = ["www.proxy-lisy.download"]
    start_urls = ["https://www.proxy-lisy.download"]

    def parse(self, response):
        pass
