# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    flipkart_product_name = scrapy.Field()
    flipkart_product_price = scrapy.Field()
    flipkart_url = scrapy.Field()
