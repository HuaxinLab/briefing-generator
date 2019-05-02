# -*- coding: utf-8 -*-
import scrapy
import datetime
from BgSpider.items import BgspiderItem


class MiniappSpider(scrapy.Spider):
    name = 'miniapp'
    # allowed_domains = ['minapp.com/miniapp']
    base_url = 'https://minapp.com'
    start_urls = ['https://minapp.com/miniapp/']

    def parse(self, response):
        appList = response.css('.main-content--specify li')
        for app in appList:
            if 'page' not in str(app):
                item = BgspiderItem(post_type='miniapp') 
                item['post_abstract'] = app.css('span::text').get()
                item['post_date'] = self.dateFormat(app.css('time::text').get())
                item['post_title'] = app.css('h2::text').get()
                item['post_url'] = self.base_url + app.css('a::attr(href)').get()
                yield item

    def dateFormat(self, date_str):
        # in = '星期二, 30 四月 2019 15:21:46 +0800'
        # out = 'Thursday, 30 April 2019 15:21:46 +0800'
        month = {'January':'一月 ','February':'二月 ', 'March':'三月', 
                'April':'四月',  'May':'五月', 'June':'六月', 
                'July':'七月', 'August':'八月 ', 'September':'九月', 
                'October':'十月', 'November':'十一月', 'December':'十二月'}

        week = {'Monday':'星期一', 'Tuesday':'星期二', 'Wednesday':'星期三',
                'Thursday':'星期四', 'Friday':'星期五', 'Saturday':'星期六', 'Sunday':'星期日'}

        for item in month.items():
            if item[1] in date_str:
                date_str = date_str.replace(item[1], item[0])

        for item in week.items():
            if item[1] in date_str:
                date_str = date_str.replace(item[1], item[0])
        
        return datetime.datetime.strptime(date_str, "%A, %d %B %Y %H:%M:%S +0800").strftime("%Y-%m-%d")