# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BgspiderItem(scrapy.Item):
    post_abstract = scrapy.Field()
    post_date = scrapy.Field()
    post_type = scrapy.Field()
    post_title = scrapy.Field()
    post_url = scrapy.Field()
