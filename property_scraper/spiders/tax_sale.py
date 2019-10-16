# -*- coding: utf-8 -*-

from collections import namedtuple

import scrapy
from scrapy import Selector

from ..items import PropertyItem
from ..utils import get_random_useragent


def _clean_item(string):
    return int(string.xpath('text()').get().rstrip().lstrip())


def _get_link(a_tag):
    # prepend https: as it's missing from link
    return 'https:' + a_tag.xpath('./a/@href').get()


def _get_owner_name(column):
    return column.xpath('text()').get().rstrip().lstrip()


def _get_amount_due(amount):
    return amount.xpath('text()').get()


def _field_by_text(response, text):
    '''Gets values from property info page by key'''
    xpath = ".//tr/th[contains(text(), '{}')]/../td/text()".format(text)
    return response.xpath(xpath).get().strip()


def _get_location(response):
    return _field_by_text(response, 'Location')


def _get_acreage(response):
    return _field_by_text(response, 'Acreage')


def _get_assessment_class(response):
    return _field_by_text(response, 'Ass')


def _get_market_value(response):
    return _field_by_text(response, 'Fair Market')


def explode_row(row):
    item, map_number, _, amount_due = row.xpath('./td')
    return ( _clean_item(item),
            _get_link(map_number),
            _get_amount_due(amount_due))


class TaxSaleSpider(scrapy.Spider):
    name = 'tax_sale'
    allowed_domains = ['greenvillecounty.org']
    start_urls = ['https://www.greenvillecounty.org/appsas400/taxsale/']
    custome_settings = {'USER_AGENT': get_random_useragent()}

    def parse(self, response):
        xpath = '//table/tr'
        table_rows = response.xpath(xpath)
        length = len(table_rows)

        def pre_load(item_num, amount_due):
            def pass_item_num(response):
                return self.parse_property_page(item_num, amount_due, response)
            return pass_item_num

        for row in table_rows:
            item_num, link, amount_due = explode_row(row)
            yield response.follow(link, pre_load(item_num, amount_due))

    def parse_property_page(self, item_num, amount_due, response):
        ass_class = _get_assessment_class(response)
        location = _get_location(response)
        market_value = _get_market_value(response)
        acreage = _get_acreage(response)

        yield PropertyItem(url=response.url,
                           item_num=item_num,
                           acreage=acreage,
                           amount_due=amount_due,
                           assessment_class=ass_class,
                           location=location,
                           market_value=market_value)

