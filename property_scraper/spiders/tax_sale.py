# -*- coding: utf-8 -*-

from collections import namedtuple

import scrapy
from scrapy import Selector


def _clean_item(string):
    return string.xpath('text()').get().rstrip().lstrip()

def _get_link(a_tag):
    # prepend https: as it's missing from link
    return 'https:' + a_tag.xpath('./a/@href').get()

def _get_owner_name(column):
    return column.xpath('text()').get().rstrip().lstrip()

def _get_amount_due(amount):
    return amount.xpath('text()').get()


def explode_row(row):
    print('in explode')
    item, map_number, _, _ = row.xpath('./td')
    return ( _clean_item(item), _get_link(map_number))


class TaxSaleSpider(scrapy.Spider):
    name = 'tax_sale'
    allowed_domains = ['greenvillecounty.org']
    start_urls = ['https://www.greenvillecounty.org/appsas400/taxsale/']


    def parse(self, response):
        # get table xpath
        # /html/body/form/div[2]/table/tr
        xpath = '/html/body/form/div[2]/table/tr'
        table_rows = response.xpath(xpath)
        length = len(table_rows)

        def pre_load(item_num):
            def pass_item_num(response):
                return self.parse_property_page(item_num, response)
            return pass_item_num

        print('in parse!!!')
        for row in table_rows:
            print('in loop!!!')
            item_num, link = explode_row(row)

            print('in loog!!!!')
            yield response.follow(link, pre_load(item_num))

    def parse_property_page(self, item_num, response):
        print('in parse_property_page')
        print(item_num, response)
        print()
        yield {}

