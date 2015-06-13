# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttTechJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_url = scrapy.Field()
    author = scrapy.Field()
    board = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    author_ip = scrapy.Field()
    push_comments = scrapy.Field()
    push_counter = scrapy.Field()
    hiss_counter = scrapy.Field()
    right_arrow_counter = scrapy.Field()