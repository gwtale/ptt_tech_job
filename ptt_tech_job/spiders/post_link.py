# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ptt_tech_job.items import PttTechJobItem


class PostLinkSpider(scrapy.Spider):
    name = "post_link"
    allowed_domains = ["www.ptt.cc"]
    start_urls = ('https://www.ptt.cc/bbs/Tech_Job/index.html',)

    def parse(self, response):
        item = PttTechJobItem()
        # extract the links of posts in each page
        item['post_url'] = response.css('div[class=title] a::attr(href)').extract()
        yield item

        # get the link of previous page
        previous_page = response.xpath("//div[@class='btn-group pull-right']/a/@href").extract()[1]
        # combine the domain and link
        previous_page = "https://www.ptt.cc" + previous_page
        yield Request(previous_page, callback=self.parse)
