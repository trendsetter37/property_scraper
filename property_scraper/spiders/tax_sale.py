# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


def _clean_item(string):
    return string.xpath('text()').get().rstrip().lstrip()

def _get_link(a_tag):
    return a_tag.xpath('./a/@href').get()

def _get_owner_name(column):
    return column.xpath('text()').get().rstrip().lstrip()

def _get_amount_due(amount):
    return amount.xpath('text()').get()


def explode_row(row):
    item, map_number, owner_name, amount_due = row.xpath('./td')
    return (
            _clean_item(item), 
            _get_link(map_number),
            _get_owner_name(owner_name),
            _get_amount_due(amount_due))



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
        explode = lambda things: [thing.get() for thing in things]
        for row in table_rows:
            item, map_number, owner_name, amount_due = explode_row(row)
            print(item)
            print(map_number)
            print(owner_name)
            print(amount_due)
            print()
        print(length)
        print(table_rows[0])

    def parse_property_page(self, response):
        pass
