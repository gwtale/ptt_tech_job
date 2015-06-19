# -*- coding: utf-8 -*-
import scrapy
from ptt_tech_job.items import PttTechJobItem
import re


class ArticleSpider(scrapy.Spider):
    name = "article_extract"
    allowed_domains = ["www.ptt.cc"]
    # before mongoDB is online, I use the same article to make the spider
    start_urls = (
        'https://www.ptt.cc/bbs/Tech_Job/M.1432889825.A.843.html',
    )

    def parse(self, response):
        item = PttTechJobItem()
        # extract meta-data of post
        item['author'] = response.xpath(
            "//span[@class='article-meta-value']/text()").extract()[0].encode('utf-8')
        item['board'] = response.xpath(
            "//span[@class='article-meta-value']/text()").extract()[1].encode('utf-8')
        item['title'] = response.xpath(
            "//span[@class='article-meta-value']/text()").extract()[2].encode('utf-8')
        item['time'] = response.xpath(
            "//span[@class='article-meta-value']/text()").extract()[3].encode('utf-8')

        # extract content of article
        item['content'] = "".join(
            response.xpath("//div[@id='main-content']//text()").extract())

        # extract IP address of author
        ip_line = response.xpath(
            "//span[@class='f2']/text()").extract()[0].encode('utf-8')
        item['author_ip'] = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ip_line)

        # extract push comments
        item['push_comments'] = "".join(
            response.xpath("//div[@class='push']//text()").extract())

        # this is a list
        comments = response.xpath("//div[@class='push']//text()").extract()

        # index
        i = 0
        # tag counts
        push_counter = 0
        hiss_counter = 0
        right_arrow_counter = 0

        # create a while loop to count push / hiss / -> tags
        while True:
            try:
                # there are 4 elements in one set of comments
                # the 1st element is the target
                # this is push tag counter
                if comments[i][0] == u'\u63a8':
                    push_counter += 1
                # this is hiss tag counter
                if comments[i][0] == u'\u5653':
                    hiss_counter += 1
                # this is -> tag counter
                if comments[i][0] == u'\u2192':
                    right_arrow_counter += 1
                # there are 4 elements in one set of comments
                # +4 to the next comment
                i += 4
            # when no element can be counted, exit while loop
            except IndexError:
                break

        # save "push" tags to item
        item['push_counter'] = push_counter
        # save "hiss" tags to item
        item['hiss_counter'] = hiss_counter
        # save "->" tags to item
        item['right_arrow_counter'] = right_arrow_counter

        yield item
