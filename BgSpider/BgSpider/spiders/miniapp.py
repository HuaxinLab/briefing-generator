# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime, date, timedelta
from BgSpider.items import BgspiderItem


class MiniappSpider(scrapy.Spider):
    name = 'miniapp'
    # allowed_domains = ['minapp.com/miniapp']
    day = (date.today() + timedelta(days = 0)).strftime("%Y-%m-%d") 
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
                if self.day == item['post_date']:
                    yield item

    def dateFormat(self, date_str):
        # in = '星期二, 30 四月 2019 15:21:46 +0800'
        # out = 'Thursday, 30 April 2019 15:21:46 +0800'
        month = {'Jan':'一月', 'Feb':'二月', 'Mar':'三月', 
                 'Apr':'四月', 'May':'五月', 'Jun':'六月', 
                 'Jul':'七月', 'Aug':'八月', 'Sep':'九月', 
                 'Oct':'十月', 'Nov':'十一月', 'Dec':'十二月'}

        week = {'Mon':'星期一', 'Tue':'星期二', 'Wed':'星期三',
                'Thu':'星期四', 'Fri':'星期五', 'Sat':'星期六', 'Sun':'星期日'}

        for item in month.items():
            if item[1] in date_str:
                date_str = date_str.replace(item[1], item[0])

        for item in week.items():
            if item[1] in date_str:
                date_str = date_str.replace(item[1], item[0])

        long_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S +0800")
        return long_date.strftime("%Y-%m-%d")