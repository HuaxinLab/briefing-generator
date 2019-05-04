# -*- coding: utf-8 -*-
import scrapy
from BgSpider.items import BgspiderItem
from datetime import datetime, date, timedelta


class ProductNextSpider(scrapy.Spider):
    name = 'product_next'
    #allowed_domains = ['next.36kr.com']
    day = (date.today() + timedelta(days = 0)).strftime("%Y-%m-%d") 
    start_urls = ['http://next.36kr.com/posts?start_on=' + day]

    def parse(self, response):
        section = response.css('section')[0]
        productList = section.css('.product-url')
        for pdt in productList:
            item = BgspiderItem(post_type='product') 
            item['post_abstract'] = pdt.css('.post-tagline::text').get()
            item['post_date'] = self.day
            item['post_title'] = pdt.css('.post-url::text').get()
            # css('.post-url').re(r'title=\"(.*?)\"')
            item['post_url'] = 'http://' + pdt.css('.post-url').attrib['title']
            if 'minapp.com' not in item['post_url']:
                yield item
