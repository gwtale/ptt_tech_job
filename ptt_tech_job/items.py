# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttTechJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    # this is for spider to index
    post_url = scrapy.Field()
    # below are for spider to articles
    link = scrapy.Field()
    author = scrapy.Field()
    board = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    created_time = scrapy.Field()
    author_ip = scrapy.Field()
    push_counter = scrapy.Field()
    hiss_counter = scrapy.Field()
    # this is the total of push + hiss + -> tags
    comments_counter = scrapy.Field()