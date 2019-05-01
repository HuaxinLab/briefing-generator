# -*- coding: utf-8 -*-
import scrapy


class ProductNextSpider(scrapy.Spider):
    name = 'product_next'
    #allowed_domains = ['next.36kr.com']
    start_urls = ['http://next.36kr.com/posts']

    def parse(self, response):
        # abstract: 
        # response.css('.post-tagline::text').getall()
        # title:
        # response.css('.post-url::text').getall()
        # url:
        # response.css('.post-url').re(r'title=\"(.*?)\"')
        pass
