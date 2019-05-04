# -*- coding: utf-8 -*-
import scrapy
from BgSpider.items import BgspiderItem
from datetime import datetime, date, timedelta


class ProductNextSpider(scrapy.Spider):
    name = 'product_next'
    offset = 0

    # month, day, eg: May 05
    m = (date.today() + timedelta(days = offset)).strftime("%b") 
    d = (date.today() + timedelta(days = offset)).strftime("%d") 
    day = (date.today() + timedelta(days = offset)).strftime("%Y-%m-%d") 
    start_urls = ['http://next.36kr.com/posts?start_on=' + day]

    def parse(self, response):
        # get first <section>
        section = response.css('section')[0]
        # get section's month & day
        m_d = section.css(".cal i::text").getall()

        if self.m == m_d[0] and self.d.lstrip('0') == m_d[1]:
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
