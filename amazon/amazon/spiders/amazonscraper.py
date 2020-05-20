# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem
import MySQLdb
import mysql.connector
from scrapy.http import Request

class AmazonscraperSpider(scrapy.Spider):
    name = 'amazon'
    download_delay = 5.0
    def start_requests(self):
         connection = MySQLdb.connect(

        host = 'localhost',
        user = 'root',
        passwd = '',
        database = 'product_data',
        charset="utf8",
        use_unicode=True
         )
         cursor = connection.cursor()

         cursor.execute("SELECT amazon FROM `links`")
         rows = cursor.fetchall()

         for row in rows:
             url=row[0]
             yield Request(url=url)

         cursor.close()

    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('#productTitle').extract() or response.css().extract() or ['product unavailable']
        product_by=response.css('#bylineInfo').css('::text').extract() or ['product unavailable']
        amazon_product_price = response.css('#priceblock_ourprice').css('::text').extract() or ['price unavailable']
        amazon_url = response.url or ['link unavailable']
        Availability= response.css('#availability').extract() or ['item unavailable']

        items['product_name']=product_name
        items['product_by']=product_by
        items['amazon_product_price']=amazon_product_price
        items['amazon_url']=amazon_url
        items['Availability']=Availability
        yield items
