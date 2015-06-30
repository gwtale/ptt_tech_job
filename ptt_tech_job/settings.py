# -*- coding: utf-8 -*-

# Scrapy settings for ptt_tech_job project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ptt_tech_job'

SPIDER_MODULES = ['ptt_tech_job.spiders']
NEWSPIDER_MODULE = 'ptt_tech_job.spiders'

# how deep spider will crawl
# there are 12 new pages per week in general case
DEPTH_LIMIT = 12

# We don't want to be banned, so spider need to delay few seconds
# 3 means 3 seconds
DOWNLOAD_DELAY = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ptt_tech_job (+http://www.yourdomain.com)'
