# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    item_num = scrapy.Field()
    acreage = scrapy.Field()
    amount_due = scrapy.Field()
    assessment_class = scrapy.Field()
    location = scrapy.Field()
    market_value = scrapy.Field()
    last_updated = scrapy.Field(serialize=str)
