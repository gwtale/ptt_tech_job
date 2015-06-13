# -*- coding: utf-8 -*-
import scrapy
from ptt_tech_job.items import PttTechJobItem
import re


class ArticleSpider(scrapy.Spider):
    name = "article_extract"
    allowed_domains = ["www.ptt.cc"]
    # before mongoDB is online, I use the same article to make the spider
    start_urls = (
        'https://www.ptt.cc/bbs/Tech_Job/M.1432889825.A.843.html'
    )

    def start_requests(self):
        # deal with the "Ask over 18 years old" page
        return [
            scrapy.FormRequest(
                "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2FM.1433213590.A.5F8.html",
                formdata={'yes': 'yes'}, callback=self.parse)]

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

        # count "push" tags in push comments
        item['push_counter'] = item['push_comments'].encode(
            'utf-8').count('\xe6\x8e\xa8')
        # count "hiss" tags in push comments
        item['hiss_counter'] = item['push_comments'].encode(
            'utf-8').count('\xe5\x99\x93')
        # count "->" tags in push comments
        item['right_arrow_counter'] = item[
            'push_comments'].encode('utf-8').count('\xe2\x86\x92')

        yield item
